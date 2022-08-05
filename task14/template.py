def n_to_p(n, p):
    res = ''
    while n > 0:
        res = '0123456789ABCDEFGHI'[n % p] + res
        n //= p
    return res


print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))