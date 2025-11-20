"""
Resources:
https://makina-corpus.com/python/python-tutorial-understanding-python-mro-class-search-path
https://docs.python.org/3/howto/mro.html
https://www.geeksforgeeks.org/python/method-resolution-order-in-python-inheritance/
"""

import sys

def mro_info(cls):
    print(cls.__mro__)
    for mro in cls.__mro__:
        print(mro)


def mro_dimond():
    class A: ...
    class B(A): ...
    class C(A): ...
    class D(C, B): ...
    mro_info(D)

def basic_example():
    class A:
        pass

    class B:
        pass

    class C(A, B):
        pass

    class D(C):
        pass

    mro_info(D)

def more_complex_example():
    """
        So, what's happened here ?
    The linearization of a class C is the sum of C plus the merge of the linearizations of the parents and the list of the parents.
    In symbolic notation:
    L[C(B1 … BN)] = C + merge(L[B1] … L[BN], B1 … BN)
    So in our case L[F(A, B)] = F + merge(L[A], L[B], A, B)

    And the algorithm to merge linearized lists is:

        Take the head of the first list, i.e L[B1][0];
        If this head is not in the tail of any of the other lists, then add it to the linearization of C and remove it from the lists in the merge,
        Otherwise look at the head of the next list and take it,
        If it is a good head. Then repeat the operation until all the class are removed or it is impossible to find good heads.
        In this case, it is impossible to construct the merge.

    L[A(X, Y)] = A + merge(L[X], L[Y], X, Y) = A, X, Y
    L[B(Y, X)] = B + merge(L[Y], L[X], Y, X) = B, Y, X

    So, L[F(A, B)] = F + merge( (A,X, Y) + (B, Y, X), A, B)
    So, applying the algorithm, A is a good head, so we keep it :
    L[F(A, B)] = F, A + merge( (X, Y) + (B, Y, X), B)
    So applaying the algorithm, X is not a good head as it appears in the tail of (B,Y, X), so we skip
    it and continue with next list to merge : (B, Y, X).
    B is a good head, so we keep it :
    L[F(A, B)] = F, A, B + merge( (X, Y) + (Y, X))
    So, applying the algorithm X is not a good head as it appears in the tail of (Y, X) so we
    skip it and jump to (Y, X). Y is not a good head too as it appears in the head of (X, Y).
    So we continue to the next list. But there is no other. Thus, Python 3 cannot
    linearize the class F to build the MRO and raise the exception!
    """

    class X:
        def who_am_I(self):
            print("I am a X")

    class Y:
        def who_am_I(self):
            print("I am a Y")

    class A(X, Y):
        def who_am_I(self):
            print("I am a A")

    class B(Y, X):
        def who_am_I(self):
            print("I am a B")

    class F(A, B):
        def who_am_I(self):
            print("I am F")

    print(F.__mro__)


def other_example():
    print('*' * 100)
    
    class A:
        pass

    class B:
        pass

    class C(A, B):
        pass

    class D(C):
        pass

    class E(B):
        pass

    class F(E, D):
        pass

    print(F.__mro__)


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    basic_example()
    # more_complex_example()
    # other_example()

    mro_dimond()


if __name__ == "__main__":
    main()
