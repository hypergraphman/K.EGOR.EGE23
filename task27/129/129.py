f = open('27-129b.txt')
n = int(f.readline())
a = [int(x) for x in f.readlines()]
kk = 13
a += a
p = [0]
for el in a:
    p.append(p[-1] + el)
mx = 0
#    [15, 22, 11, 32,  31,  15,  22,  11,  32,  31]
# [0, 15, 37, 48, 80, 111, 126, 148, 159, 191, 222]
#  0   1   2   3   4    5    6    7    8    9   10
# print(p)
for k in range(n // kk * kk, kk - 1, -kk):
    for i in range(len(p) - k):
        t = p[i + k] - p[i]
        if t % kk == 0 and t > mx:
            mx = t
    if mx != 0:
        break
print(mx)