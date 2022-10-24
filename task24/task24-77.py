line = open('k8-1.txt').readline()
ans = 1
k = 1
for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        k += 1
        if ans < k:
            ans = k
    else:
        k = 1

print(ans)