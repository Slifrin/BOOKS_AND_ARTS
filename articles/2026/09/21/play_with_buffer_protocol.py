"""
https://docs.python.org/3/c-api/buffer.html
https://docs.python.org/3/reference/datamodel.html#python-buffer-protocol
https://docs.python.org/3/builtins/stdtypes.html#typememoryview


Certain objects available in Python wrap access to an underlying memory array or buffer.
Such objects include the built-in bytes and bytearray, and some
extension types like array.array. Third-party libraries may define their own types for special
purposes, such as image processing or numeric analysis.
...
It is then desirable, in some situations, to access that buffer directly and without intermediate copying.

------------------

Emulating buffer types in pure Python: __buffer__ / __release_buffer__ (PEP 688).

Requires Python 3.12+.

Before 3.12 the buffer protocol was reachable only from C (tp_as_buffer ->
bf_getbuffer / bf_releasebuffer). PEP 688 exposes it to Python code as two
dunders:

    __buffer__(self, flags: int) -> memoryview
        Called when a consumer requests a buffer (memoryview(obj), bytes(obj),
        file.write(obj), socket.send(obj), struct.unpack_from(fmt, obj),
        hashlib.sha256(obj), np.frombuffer(obj), ...).
        `flags` is an int; compare against inspect.BufferFlags.
        Must return a memoryview backed by the object's own memory.

    __release_buffer__(self, view: memoryview) -> None
        Optional. Called exactly once per successful __buffer__ call, when the
        consumer is done. `view` is the identical object __buffer__ returned.
        This is where you undo whatever the export pinned (locks, refcounts,
        "no resize while exported" guards).

Run:  python3.13 buffer_protocol_demo.py
"""

from __future__ import annotations

import hashlib
import inspect
import io
import struct
import sys
from collections.abc import Buffer  # PEP 688 ABC: isinstance() works via __buffer__

if sys.version_info < (3, 12):
    raise SystemExit("PEP 688 requires Python 3.12+; got %s" % sys.version.split()[0])


def describe_flags(flags: int) -> str:
    """Render request flags as a name, e.g. 284 -> 'FULL_RO'.

    BufferFlags is an IntFlag, so iterating the class yields only the
    single-bit members; the composite names (FULL_RO, RECORDS, CONTIG, ...)
    live in __members__ as aliases.
    """
    bf = inspect.BufferFlags
    for name, value in bf.__members__.items():
        if int(value) == flags:
            return f"{name} ({flags})"
    parts = [
        m.name
        for m in (
            bf.WRITABLE,
            bf.FORMAT,
            bf.ND,
            bf.STRIDES,
            bf.C_CONTIGUOUS,
            bf.F_CONTIGUOUS,
            bf.ANY_CONTIGUOUS,
            bf.INDIRECT,
        )
        if flags & m == m and m != 0
    ]
    return f"{'|'.join(parts) or 'SIMPLE'} ({flags})"


# ---------------------------------------------------------------------------
# 1. The minimal read-only case
# ---------------------------------------------------------------------------


class ReadOnlyBlob:
    """Smallest useful implementation: expose an internal bytearray read-only.

    Note the two rules that keep this correct:
      * a request *with* WRITABLE is refused with BufferError,
      * a request *without* WRITABLE gets .toreadonly(), so the consumer
        physically cannot write through it.
    """

    def __init__(self, data: bytes | bytearray) -> None:
        self._data = bytearray(data)

    def __buffer__(self, flags: int) -> memoryview:
        print(f"    ReadOnlyBlob.__buffer__ flags={describe_flags(flags)}")
        if flags & inspect.BufferFlags.WRITABLE:
            raise BufferError("ReadOnlyBlob is not writable")
        return memoryview(self._data).toreadonly()

    def __release_buffer__(self, view: memoryview) -> None:
        print("    ReadOnlyBlob.__release_buffer__")
        view.release()


# ---------------------------------------------------------------------------
# 2. The real reason __release_buffer__ exists: pinning memory while exported
# ---------------------------------------------------------------------------


class Frame:
    """A resizable byte store that refuses to move its memory while exported.

    This mirrors what bytearray does in C: `bytearray` raises
    "BufferError: Existing exports of data: object cannot be re-sized" because
    reallocating would leave every live memoryview pointing at freed memory.
    Tracking that in Python is exactly what __release_buffer__ is for.

    It also supports writable exports, so readinto()/recv_into() work.
    """

    def __init__(
        self, data: bytes | bytearray = b"", *, allow_write: bool = True
    ) -> None:
        self._data = bytearray(data)
        self._allow_write = allow_write
        self._exports: list[memoryview] = []  # live views, newest last
        self._writable_exports = 0

    # -- buffer protocol ----------------------------------------------------

    def __buffer__(self, flags: int) -> memoryview:
        # Flag convention, which is easy to get backwards:
        #   flags & WRITABLE  -> the caller *requires* writable memory;
        #                        raise BufferError if we cannot provide it.
        #   no WRITABLE bit   -> the caller *accepts* read-only; it does NOT
        #                        ask us to downgrade. bytearray returns a
        #                        writable buffer either way, which is why
        #                        memoryview(bytearray(3))[0] = 1 works even
        #                        though memoryview() requests FULL_RO (284).
        # So writability follows from what the object *is*, not from the flags.
        if flags & inspect.BufferFlags.WRITABLE and not self._allow_write:
            raise BufferError("Frame was created read-only")

        view = memoryview(self._data)
        if not self._allow_write:
            view = view.toreadonly()

        self._exports.append(view)
        self._writable_exports += not view.readonly
        print(
            f"    Frame.__buffer__  {describe_flags(flags)} "
            f"-> exports={len(self._exports)}, readonly={view.readonly}"
        )
        return view

    def __release_buffer__(self, view: memoryview) -> None:
        # `view` is guaranteed to be the very object __buffer__ returned,
        # so identity comparison is the right lookup.
        for i, held in enumerate(self._exports):
            if held is view:
                del self._exports[i]
                break
        else:  # pragma: no cover - would mean an interpreter bug
            raise AssertionError("released a view we never exported")
        self._writable_exports -= not view.readonly
        view.release()
        print(f"    Frame.__release_buffer__ -> exports={len(self._exports)}")

    # -- ordinary API that has to respect live exports ----------------------

    @property
    def exports(self) -> int:
        return len(self._exports)

    def resize(self, n: int) -> None:
        if self._exports:
            raise BufferError(
                f"cannot resize Frame: {len(self._exports)} existing export(s)"
            )
        if n < len(self._data):
            del self._data[n:]
        else:
            self._data.extend(b"\0" * (n - len(self._data)))

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Frame({bytes(self._data)!r}, exports={len(self._exports)})"


# ---------------------------------------------------------------------------
# Demos
# ---------------------------------------------------------------------------


def demo_readonly() -> None:
    print("\n=== 1. read-only blob feeding stdlib consumers ===")
    blob = ReadOnlyBlob(b"PEP-688 buffers")

    print("  isinstance(blob, collections.abc.Buffer):", isinstance(blob, Buffer))

    print("  bytes(blob):")
    print("   ->", bytes(blob))

    print("  hashlib.sha256(blob):")
    print("   ->", hashlib.sha256(blob).hexdigest()[:16], "...")

    print("  BytesIO().write(blob):")
    sink = io.BytesIO()
    n = sink.write(blob)
    print("   -> wrote", n, "bytes")

    print("  struct.unpack_from('<4s', blob):")
    print("   ->", struct.unpack_from("<4s", blob))

    print("  memoryview(blob) is read-only, so writing fails:")
    with memoryview(blob) as mv:
        print("   -> mv.readonly =", mv.readonly, ", mv[:3] =", bytes(mv[:3]))
        try:
            mv[0] = 0x00
        except TypeError as exc:
            print("   -> TypeError:", exc)

    print("  a consumer that demands a writable buffer is refused:")
    try:
        io.BytesIO(b"xxxxx").readinto(blob)
    except (BufferError, TypeError) as exc:
        # readinto() reports the refusal as TypeError; memoryview(obj, ...)
        # and most other consumers let the BufferError propagate as-is.
        print(f"   -> {type(exc).__name__}: {exc}")


def demo_writable() -> None:
    print("\n=== 2. writable export: readinto() fills our memory in place ===")
    frame = Frame(bytearray(8))
    print("  before:", frame)

    src = io.BytesIO(b"abcdefgh-ignored-tail")
    n = src.readinto(frame)  # requests WRITABLE, writes through
    print(f"   -> readinto wrote {n} bytes; frame = {frame}")

    print("  mutate through an explicit writable memoryview:")
    with memoryview(frame) as mv:
        mv[0:3] = b"XYZ"
    print("   -> frame =", frame)

    print("  typed view over the same memory via memoryview.cast:")
    # cast() needs a *native* single-character format ('H', not '<H').
    with memoryview(frame).cast("H") as words:  # 8 bytes -> 4 native uint16
        print("   -> as uint16:", list(words))
        words[0] = 0x4142
    print("   -> after words[0] = 0x4142:", frame)


def demo_release_semantics() -> None:
    print("\n=== 3. __release_buffer__ and the resize guard ===")
    frame = Frame(b"0123456789")

    print("  resize with no exports is fine:")
    frame.resize(12)
    print("   -> len =", len(frame))

    print("  take two overlapping exports:")
    a = memoryview(frame)
    b = memoryview(frame)
    print("   -> frame.exports =", frame.exports)

    print("  resizing now must fail (the C bytearray behaviour):")
    try:
        frame.resize(4)
    except BufferError as exc:
        print("   -> BufferError:", exc)

    print("  releasing views calls __release_buffer__ once each:")
    a.release()
    b.release()
    print("   -> frame.exports =", frame.exports)

    print("  and now resize works again:")
    frame.resize(4)
    print("   -> frame =", frame)

    print("  release is also driven by refcount/GC, not just .release():")
    memoryview(frame)  # dropped immediately -> __release_buffer__ runs
    print("   -> frame.exports =", frame.exports)

    print("  bytes(frame) acquires and releases within the one call:")
    print("   ->", bytes(frame), "exports now", frame.exports)


def demo_flags() -> None:
    print("\n=== 4. what flags different consumers actually request ===")

    class FlagSpy:
        def __init__(self, data: bytes) -> None:
            self._data = bytearray(data)

        def __buffer__(self, flags: int) -> memoryview:
            print(f"   requested {describe_flags(flags)}")
            return memoryview(self._data)  # bytearray-backed: always writable

        def __release_buffer__(self, view: memoryview) -> None:
            view.release()

    spy = FlagSpy(b"12345678")
    print("  memoryview(obj):")
    memoryview(spy).release()
    print("  bytes(obj):")
    bytes(spy)
    print("  BytesIO().write(obj):")
    io.BytesIO().write(spy)
    print("  BytesIO(...).readinto(obj):")
    io.BytesIO(b"xxxxxxxx").readinto(spy)

    print("\n  inspect.BufferFlags values (including composite aliases):")
    for name, value in inspect.BufferFlags.__members__.items():
        print(f"   {name:<15} = {int(value):>4}  0b{int(value):09b}")


def demo_failure_modes() -> None:
    print("\n=== 5. failure modes worth knowing ===")

    class NotAMemoryview:
        def __buffer__(self, flags: int):
            return b"oops"  # must be a memoryview

    print("  __buffer__ returning non-memoryview:")
    try:
        memoryview(NotAMemoryview())
    except TypeError as exc:
        print("   -> TypeError:", exc)

    class LiesAboutWritable:
        def __init__(self) -> None:
            self._data = b"immutable"  # bytes: read-only storage

        def __buffer__(self, flags: int) -> memoryview:
            return memoryview(self._data)  # never writable

    print("  WRITABLE requested but a read-only view returned:")
    try:
        io.BytesIO(b"xxxxxxxxx").readinto(LiesAboutWritable())
    except (BufferError, TypeError) as exc:
        print(f"   -> {type(exc).__name__}: {exc}")

    class Dangling:
        """Anti-pattern: exporting memory not owned by (or tied to) self."""

        def __buffer__(self, flags: int) -> memoryview:
            return memoryview(bytearray(4))  # temp dies with the view

    print("  exporting a temporary works here but is fragile:")
    print("   ->", bytes(Dangling()), "(fine only because the view keeps it alive)")

    class OverRestrictive:
        """Anti-pattern: downgrading to read-only whenever WRITABLE is absent.

        memoryview(obj) asks for FULL_RO (284), which has no WRITABLE bit, so
        this class hands back a read-only view and breaks the ordinary
        `memoryview(obj)[0] = x` that works on bytearray.
        """

        def __init__(self) -> None:
            self._data = bytearray(4)

        def __buffer__(self, flags: int) -> memoryview:
            mv = memoryview(self._data)
            return mv if flags & inspect.BufferFlags.WRITABLE else mv.toreadonly()

    print("  downgrading on absent WRITABLE breaks memoryview() writes:")
    with memoryview(OverRestrictive()) as mv:
        try:
            mv[0] = 1
        except TypeError as exc:
            print("   -> TypeError:", exc, "(bytearray would have allowed this)")

    print("  __buffer__ may refuse a shape it cannot provide:")

    class ContiguousOnly:
        def __init__(self) -> None:
            self._data = bytearray(b"contig")

        def __buffer__(self, flags: int) -> memoryview:
            if flags & inspect.BufferFlags.INDIRECT == inspect.BufferFlags.INDIRECT:
                raise BufferError("no indirect (PIL-style) buffers here")
            return memoryview(self._data).toreadonly()

    try:
        memoryview(ContiguousOnly())  # memoryview asks for FULL_RO (284)
    except BufferError as exc:
        print("   -> BufferError:", exc)
    # hashlib asks for SIMPLE (0), so the same object serves it fine.
    digest = hashlib.sha256(ContiguousOnly()).hexdigest()[:16]
    print("   -> but hashlib (SIMPLE) is happy:", digest, "...")


if __name__ == "__main__":
    print(f"Python {sys.version.split()[0]}")
    demo_readonly()
    demo_writable()
    demo_release_semantics()
    demo_flags()
    demo_failure_modes()
    print("\nDone.")
