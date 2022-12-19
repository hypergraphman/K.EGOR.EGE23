f = open('test.txt')
n, m = map(int, f.readline().split())
s = dict()
for _ in range(n):
    y, x = map(int, f.readline().split())
    if y in s:
        s[y].append(x)
    else:
        s[y] = [x]

c = 0
for y in range(n):
    if m > sum(s[y]):
        c += 1
    else:

print(c)


