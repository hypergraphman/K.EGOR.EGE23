k = 157
f = open("27_B.txt")
n = int(f.readline())
data = list(map(int, f.readlines()))
mx = 0
ln = 0
t_s = [0] + [None] * (k-1)
t_l = [0]*k
tt_s = 0
for i in range(n):
    tt_s += data[i]
    x = tt_s % k
    if t_s[x]:
        if mx < tt_s - t_s[x] or mx == tt_s - t_s[x] and ln > i - t_l[x]:
            mx = tt_s - t_s[x]
            ln = i - t_l[x]
    else:
        t_s[x] = tt_s
        t_l[x] = i


print(ln)



