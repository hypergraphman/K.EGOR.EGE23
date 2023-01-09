f = open('test.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))
# print(data)
# print(n, len(data))
mx = 0
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        sm = sum(data[i:j])
        ln = j - i
        if sm % 43 == 0 and sm > mx:
            mx = sm
            ans = ln
            print(i, j)
        if sm % 43 == 0 and sm == mx and ln < ans:
            ans = ln
            print(i, j)
print(ans)

# 185 844158