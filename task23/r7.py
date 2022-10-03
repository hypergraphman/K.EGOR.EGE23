a = [0] * 10000
a[30] = 1
for i in range(30, 12, -1):
    if i - 1 >= 12:
        a[i - 1] += a[i]
    if i // 2 >= 12:
        a[i // 2] += a[i]
print(a[12])
for i in range(12, 1, -1):
    if i - 1 >= 1:
        a[i - 1] += a[i]
    if i // 2 >= 1:
        a[i // 2] += a[i]
print(a[1])

