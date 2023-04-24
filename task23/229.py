def f(s, e, p):
    if s == e:
        all_p.append(p)
        return 1
    if s < e:
        return 0
    return f(s - 1, e, p + 'A') + f(s - 2, e, p + 'B') + f(s // 2, e, p + 'C')


all_p = []
print(f(34, 2, ''))1

from fnmatch import fnmatch
k = 0
for p in all_p:
    if 'AA' not in p and 'BB' not in p and 'CC' not in p and fnmatch(p, '?A*CB?'):
        k += 1
print(k)