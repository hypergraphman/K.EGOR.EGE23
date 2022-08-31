def check(p1, p2, p3):
    return p1 + p2 + p3 < mxx


a = list(map(int, open('17-273.txt').readlines()))
mxx = max(a)
mx = -10**16
mn = 10**16
count = 0
for i in range(len(a) - 2):
    x1, x2, x3 = a[i], a[i + 1], a[i + 2]
    if check(x1, x2, x3):
        count += 1
        if mx < max(x1, x2, x3):
            mx = max(x1, x2, x3)
        if mn > min(x1, x2, x3):
            mn = min(x1, x2, x3)
print(count, mx + mn)
