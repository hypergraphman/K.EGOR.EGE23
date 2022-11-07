def divs(n):
    if n == 0:
        return []
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


for i in range(1000):
    d = divs(i)
    if len(d) == 2:
        print(i)