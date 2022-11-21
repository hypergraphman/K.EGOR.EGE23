f = open('26-k1.txt')
v, n = map(int, f.readline().split())
data = sorted(map(int, f.readlines()))
# print(data)
# print(data[len(data) - 4])
s = data[-(n + 1)]
k = sum(data[-n:]) * 0.2
print(s, k)
