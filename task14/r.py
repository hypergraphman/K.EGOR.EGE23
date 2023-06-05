from string import ascii_uppercase, digits
D = digits + ascii_uppercase


def n_to_p(n, p):
    r = ''
    while n > 0:
        r = D[n % p] + r
        n //= p
    return r


# r25
print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))
# r24
print(n_to_p(64**10 + 2**90 - 16, 8).count('7'))
# 314
print(sum(map(int, n_to_p((7**160 * 7**90) - (14**150 + 2**13), 7).replace('6', '0'))))
