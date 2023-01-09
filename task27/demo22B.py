f = open('27_B.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))
# print(data)
# print(n, len(data))
sm = 0
k = 0
for i in range(2857142 + 1, n):
    if data[i] == 1:
        break
    sm += data[i]
    k += 1
print(sm, sm % 43, i, k)

# 744080213 0 1442152
# 684064511 0 2768407
# 45635040 0 2857142
# 744080256 0 3701301 844158
# 744080256 0 4782926 1081625