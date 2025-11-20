Steps to inline incrementation of variable

```python3
>>> def inc(x):
...     x += 1
...
>>> import dis
>>> dis.dis(inc)
  1           RESUME                   0

  2           LOAD_FAST                0 (x)
              LOAD_CONST               1 (1)
              BINARY_OP               13 (+=)
              STORE_FAST               0 (x)
              RETURN_CONST             0 (None)
```