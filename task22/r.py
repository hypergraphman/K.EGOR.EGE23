d = dict()
for line in open('22-28.txt'):
    n, t, z = line.split('\t')
    t = int(t)
    z = z.strip().strip('"').split('; ')
    d[n] = [t, z]
    if z[0] != '0':
        mx = 0
        for el in z:
            if d[el][0] > mx:
                mx = d[el][0]
        d[n][0] += mx
print(max(d.values(), key=lambda x: x[0])[0])