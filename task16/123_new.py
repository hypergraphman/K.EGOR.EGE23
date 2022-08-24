def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return 1 + f(n // 3)
    return f(n // 3)


def n_to_p(n, p):
    res = ''
    while n > 0:
        res = '0123456789ABCDEFGHI'[n % p] + res
        n //= p
    return res


# for i in range(100):
#     print(n_to_p(i, 3), f(i))
print(n_to_p(100_000_000, 3))
# 5201982