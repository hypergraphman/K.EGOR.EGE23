win = 140
start = 4


def f(a, b, c, m):
    if a * b >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(a + 1, b, c + 1, m),
             f(a, b + 1, c + 1, m),
             f(a * 2, b, c + 1, m),
             f(a, b * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for b in range(1, 34 + 1):
    for m in range(1, 4 + 1):
        if f(start, b, 0, m):
            print(b, m)