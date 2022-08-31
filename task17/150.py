a = list(map(int, open('17-1.txt').readlines()))
mn = 10**16
count = 0
for i in range(len(a) - 1):
    x1, x2 = a[i], a[i + 1]
    if x1 % 7 == 0 and x2 % 17 != 0 or x2 % 7 == 0 and x1 % 17 != 0:
        count += 1
        if mn > x1 + x2:
            mn = x1 + x2
print(count, mn)