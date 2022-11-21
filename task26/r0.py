f = open('26.txt')
v, n = map(int, f.readline().split())
data = sorted(map(int, f.readlines()))
# print(data)
users = 0
while v - data[users] >= 0:
    v -= data[users]
    users += 1
print(users)
mx_file = v + data[users - 1]
mx = 0
i = users - 1
while data[i + 1] < mx_file:
    i += 1
print(data[i])