f = open('26-51.txt')
n = int(f.readline())
a = sorted(map(int, f.readlines()))
k = 0
mx = 0
for i in range(n - 1):
    for j in range(i + 1 + 100, n):
        if (a[i] + a[j]) % 2 == 0:
            k += 1
            mx = max(a[i] + a[j], mx)
print(k, mx / 2)
