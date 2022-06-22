from itertools import permutations


def f(n):
    all_pairs = []
    for d1, d2 in permutations(str(n), 2):
        num = int(d1 + d2)
        if num >= 10:
            all_pairs.append(num)
    return max(all_pairs) - min(all_pairs)


for i in range(100, 1000):
    if f(i) == 40:
        print(i)
        break