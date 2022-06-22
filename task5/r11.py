def f(n):
    s1 = f'{n:b}'
    s2 = s1[1:]
    s3 = int(s2, 2)
    return n - s3


a = set()
for i in range(500, 5000 + 1):
    a.add(f(i))
print(a)
print(len(a))