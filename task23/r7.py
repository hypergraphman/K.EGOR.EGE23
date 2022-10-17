a = [0] * 10000
a[1] = 1
for i in range(1, 410):
    if i + 1 <= 410:
        a[i + 1] += a[i]
    if i * 5 <= 410:
        a[i * 5] += a[i]
    if (i * 10 + 1) % 3 == 0 and i * 10 + 1 <= 410:
        a[i * 10 + 1] += a[i]
print(a[410])

