f = open('27-157b.txt')
n, k = map(int, f.readline().split())
a = [0] * 400_000
for i in range(n):
    time, v = map(int, f.readline().split())
    a[time] = v
temp = a[:k]
mx = 0
mx_odd = 0
mx_even = 0
for i in range(k, 400_000):
    d = i % k
    if temp[d] % 2 == 0:
        if temp[d] > mx_even:
            mx_even = temp[d]
    else:
        if temp[d] > mx_odd:
            mx_odd = temp[d]

    if a[i] % 2 == 0:
        if a[i] + mx_even > mx:
            mx = a[i] + mx_even
    else:
        if a[i] + mx_odd > mx:
            mx = a[i] + mx_odd
    temp[d] = a[i]
print(mx)
