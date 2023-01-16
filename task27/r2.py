f = open('test.txt')
n = int(f.readline())
p = 12
k = [0] * p
k1 = k[:]
for _ in range(n):
    x = int(f.readline())
    for j in range(p):
        k1[(j + x) % p] += k[j]
    k1[x % p] += 1
    k = k1[:]
print(k[0])
