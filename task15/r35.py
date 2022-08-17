for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        Q = x % a != 0
        W = x % 6 == 0
        E = x % 9 != 0
        f = Q <= (W <= E)
        if not f:
            is_a = False
            break
    if is_a:
        print(a)

print('-------------')

for a in range(1, 100):
    if all((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) for x in range(1, 1000)):
        print(a)