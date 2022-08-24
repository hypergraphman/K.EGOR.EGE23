from datetime import datetime
from functools import cache


@cache
def f(x):
    if x == 1 or x == 2:
        return 1
    return f(x - 1) + f(x - 2)


n = int(input())
s1 = datetime.now()
print(f(n))
s2 = datetime.now()
print(s2 - s1)