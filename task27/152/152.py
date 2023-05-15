f = open('27-152b.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))
zeros = 5
d = [[0] * (zeros + 2) for _ in range(zeros + 2)]
for el in data:
    n5 = 0
    while el % 5 == 0 and n5 <= zeros:
        n5 += 1
        el //= 5
    n2 = 0
    while el % 2 == 0 and n2 <= zeros:
        n2 += 1
        el //= 2
    d[n2][n5] += 1

print(d)
s = 0
for i in range(zeros + 2):
    for j in range(zeros + 2):
        for k in range(zeros + 2):
            for q in range(zeros + 2):
                if min(i + k, j + q) == zeros:
                    s += d[i][j] * d[k][q]
print(s // 2)



