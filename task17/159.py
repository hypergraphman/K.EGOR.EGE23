def check(p1, p2):
    return (p1 + p2) % 3 == 0 and (p1 + p2) % 6 != 0 and abs(p1 * p2) % 10 == 8


a = list(map(int, open('17-3.txt').readlines()))
mx = -10**16
count = 0
for i in range(len(a) - 1):
    x1, x2 = a[i], a[i + 1]
    if check(x1, x2):
        count += 1
        if mx < x1 + x2:
            mx = x1 + x2
print(count, mx)

