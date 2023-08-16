# Some examples

```python
from timeit import timeit
timeit("factorial(999)", "from math import factorial", number=10)


from math import factorial
timeit(lambda: factorial(999), number=10)
```
