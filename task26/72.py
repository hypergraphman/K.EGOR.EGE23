f = open('26-72.txt')
n, m, k = map(int, f.readline().split())
s = dict()
for _ in range(k):
    y, x = map(int, f.readline().split())
    if y in s:
        s[y].append(x)
    else:
        s[y] = [0, x, n + 1]

for r in s:
    s[r].sort()

print(s)

count = 0
mx_r = 0
mx = 0
for r in range(1, m + 1):
    count_r = 0
    if r in s:
        for i in range(1, len(s[r])):
            empty = s[r][i] - s[r][i - 1] - 1
            if empty - 3 > 0:
                count_r += empty - 3
    else:
        count_r = n - 3
    count += count_r
    if count_r > mx:
        mx = count_r
        mx_r = r
print(count, mx_r)