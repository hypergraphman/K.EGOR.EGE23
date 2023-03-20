with open('27-42b.txt') as f:
    n = int(f.readline())
    s1 = s2 = s3 = 0
    z = []
    for i in range(1, n + 1):
        p1, p2, p3, = sorted(map(int, f.readline().split()))
        s1 += p1
        s2 += p2
        s3 += p3
        # print(p1, p2, p3, p3 - p2, p3 - p1)
        z1 = 10**10
        if p3 % 2 != p2 % 2:
            z1 = p3 - p2
        z2 = 10 ** 10
        if p3 % 2 != p1 % 2:
            z2 = p3 - p1
        z.append((min(z1, z2), i))
z.sort()
print(s1, s2, s3)
print(z[0], z[1])
print(s3 - z[0][0] - z[1][0])
