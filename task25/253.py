def divs(n):
    if n == 0:
        return []
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


for i in range(2000000, 3000000):
    d = divs(i)
    c = 1
    for k in d:
        c = c * k
    if sum(d) % 2 == 1 and len(d) > 30 and c % 2 == 1:
        print(i)
        for num in d:
            if len(divs(num)) == 2:
                print(num, end=' ')
        print()