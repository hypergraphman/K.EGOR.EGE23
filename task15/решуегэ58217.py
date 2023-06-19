def treug(n, m, k):
    s = sorted((n, m, k))
    return s[2] < s[1] + s[0]


for a in range(1, 10000):
    if all(not ((treug(x, 11, 16) == (not (max(x, 5) > 10))) and treug(4, a, x)) for x in range(1, 10000)):
        print(a)