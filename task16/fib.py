f_prev, f = 1, 1
n = int(input())
i = 2
while i < n:
    f_prev, f = f, f + f_prev
    i += 1
print(f)
print(354224848179261915075)