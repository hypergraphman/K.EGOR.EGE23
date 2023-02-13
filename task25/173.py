from functools import lru_cache


@lru_cache(None)
def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)

    return len(d)


@lru_cache(None)
def s(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if f(i) == 0:
                d.add(i)
            if f(n // i) == 0:
                d.add(n // i)
    if len(d) != 0:
        return sum(d) // len(d)
    return 0


i = 650000
k = 4
while k != 0:
    if s(i) % 37 == 23 and s(i) > 0:
        print(i, s(i))
        k -= 1
    i += 1