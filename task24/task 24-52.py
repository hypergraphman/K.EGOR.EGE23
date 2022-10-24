line = open('k8-0.txt').readline()
ans = 1
k = 1
l = 0
for i in range(len(line) - 1):
    if line[i] == line[i + 1]:
        k += 1
        if ans < k:
            ans = k
            l = line[i]
    else:
        k = 1

print(l, ans)