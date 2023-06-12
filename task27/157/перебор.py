f = open('27-157b.txt')
n, k = map(int, f.readline().split())
a = []
mx = 0
for i in range(n):
    a += list(map(int, f.readline().split()))
for i in range(0, len(a) - 3, 2):
    for j in range(i + 2, len(a) - 1, 2):
        x1, x2, x3, x4 = a[i], a[i + 1], a[j], a[j+1]
        if x3 - x1 >= k and (x2 + x4)%2 == 0  and x2 + x4 > mx:
            mx = x2 + x4

print(mx)
