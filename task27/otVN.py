k = 157
f = open("27_A.txt")
n = int(f.readline())
print(n)
data = list(map(int, f.readlines()))
mx = 0
ln = 0
for i in range(n):
    for j in range(i, n):
        t = data[i:j+1]
        if sum(t) % k == 0 and (mx < sum(t) or sum(t) == mx and ln > len(t)):
            mx = sum(t)
            ln = len(t)


print(ln)

