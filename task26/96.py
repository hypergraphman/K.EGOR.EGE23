f = open('26-96.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    lat, long = f.readline().split()
    lat = lat[:-1]
    if '' == lat or '-' == lat:
        lat = 0
    else:
        lat = int(lat)
    long = int(long)
    if long not in d:
        d[long] = list()
    d[long].append(lat)
ans = sorted(d.items(), key=lambda x: (-len(x[1]), -x[0]))[0]
print(ans[0], len(set(ans[1])))
