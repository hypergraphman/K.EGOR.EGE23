f = open('26-j1.txt')
n = int(f.readline())
data = map(int, f.readlines())
d = dict()
for i in range(1, 100):
    d[i] = 0
for i in data:
    d[i] += 1
s = 0
for i in range(1, 50):
    s += min(d[i], d[100 - i])
s += d[50] // 2
print(s)

