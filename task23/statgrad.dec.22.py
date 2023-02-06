def f(start, fin, turn):
    if start > fin:
        return 0
    if '111' in turn or '222' in turn:
        return 0
    if start == fin:
        print(turn)
        return 1
    return f(start + 1, fin, turn + '1') + f(start * 2, fin, turn + '2')


print(f(1, 16, ''))