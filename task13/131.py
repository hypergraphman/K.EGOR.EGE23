g = {
    'A': 'B',
    'B': 'V',
    'V': 'YEG',
    'G': 'ED',
    'D': 'EYK',
    'E': 'Y',
    'Y': 'NZ',
    'Z': 'LKD',
    'M': 'NZA',
    'K': 'L',
    'L': 'M',
    'N': 'ABV',
}


def find_path(s, p):
    if len(p) > 1 and p[0] == p[-1]:
        paths.add(p)
        return
    if len(set(p)) < len(p):
        return
    for v in g[s]:
        find_path(v, p + v)


paths = set()
find_path('Y', 'Y')
print(len(paths))
