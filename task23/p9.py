a = [0] * 10000
a[1] = 1
for i in range(1, 10):
    if i + 1 <= 10:
        a[i + 1] += a[i]
    if i * 2 <= 10:
        a[i * 2] += a[i]
print(a[10])
for i in range(10, 20):
    if i + 1 <= 20:
        a[i + 1] += a[i]
    if i * 2 <= 20:
        a[i * 2] += a[i]
print(a[20])
