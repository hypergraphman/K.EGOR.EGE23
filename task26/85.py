FREE = 100
H = 500


def is_free_place(a):
    a.sort()
    for i in range(len(a) - 1):
        if a[i][1] == a[i + 1][1] and a[i + 1][0] - a[i][0] - 1 == FREE:
            return True
    return False


def is_city_h(a):
    k = 0
    for place, city in a:
        if city == 0:
            k += 1
    return k >= H


def count_city_other(a):
    k = 0
    for place, city in a:
        k += city
    return k


f = open('26-85.txt')
d = dict()
n = int(f.readline())
for i in range(n):
    row, place, city = map(int, f.readline().split())
    if row in d:
        d[row].append((place, city))
    else:
        d[row] = [(place, city)]

find_row = None
for row, a in sorted(d.items(), key=lambda x: x[0]):
    if is_free_place(a) and is_city_h(a):
        find_row = row

print(find_row, count_city_other(d[find_row]))
