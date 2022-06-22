def f(n):
    s1 = f'{n:b}'
    s2a = s1 + str(sum(map(int, s1)) % 2)
    s2b = s2a + str(sum(map(int, s2a)) % 2)
    return int(s2b, 2)


for i in range(1000):
    if f(i) > 77:
        print(i)
        break
