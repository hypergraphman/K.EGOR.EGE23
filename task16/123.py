def f(n):
    if n == 0:
        return 8
    if n > 0 and n % 3 == 0:
        return 5 + f(n // 3)
    return f(n // 3)


count = 0
for i in range(1, 100_000_000 + 1):
    try:
        if f(i) == 18:
            count += 1
    except:
        pass
print(count)
