f = open('test.txt')
m, n = int(f.readline())
data = list(map(int, f.readlines()))
mn = 10000*3000000
for i in range(n, len(data)):
    for k in range(i):
        s = data[k] + data[k+1] + data[k+2]
        if s % 131 == 0:
            if s < mn:
                mn = s
print(mn)

