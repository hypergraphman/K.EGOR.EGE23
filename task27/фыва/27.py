f = open('test27')
n, d = map(int, f.readline().split())
a = dict()
mx_sr = 0
mn_sr = 10**10
for i in range(n):
    k, p1, p2, p3 = map(int, f.readline().split())
    if k not in a:
        a[k] = [0, 0]
    a[k][0] += max((p1, p2, p3))
    a[k][1] += 1

for k in a.keys():
    s_r, s_p = a[k]
    sr = s_r / s_p
    if s_p > d:
        mx_sr = max(sr, mx_sr)
        mn_sr = min(sr, mn_sr)
print(mx_sr - mn_sr)






