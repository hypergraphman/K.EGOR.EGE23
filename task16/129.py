def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return 1 + f(n // 2)
    return f(3 * n + 1) + 1


count = 0
for i in range(1, 100_000 + 1):
    try:
        if f(i) == 16:
            count += 1
    except:
        pass
print(count)