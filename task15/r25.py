for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        Q = x & 125 != 1
        W = x & 34 == 2
        E = x & a == 0
        f = Q or (W <= E)
        if not f:
            is_a = False
            break
    if is_a:
        print(a)
        break

print('-------------')

for a in range(1, 100):
    if all((x & 125 != 1) or ((x & 34 == 2) <= (x & a == 0)) for x in range(1, 1000)):
        print(a)
        break