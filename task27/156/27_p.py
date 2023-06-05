f = open('27-156a.txt')
n, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))

mn = float('inf')
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if j - i + 1 >= k and s % 131 == 0 and s < mn:
            mn = s

print(mn)
