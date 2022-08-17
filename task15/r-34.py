for a in range(1, 100):
    is_a = True
    for k in range(1, 100):
        for n in range(1, 100):
            f = (5 * k + 6 * n > 57) or ((k <= a) and (n < a))
            if not f:
                is_a = False
                break
    if is_a:
        print(a)
        break

print('-------------')

for a in range(1, 100):
    if all((5 * k + 6 * n > 57) or ((k <= a) and (n < a)) for k in range(1, 100) for n in range(1, 100)):
        print(a)
        break