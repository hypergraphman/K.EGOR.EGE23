line = open('24.txt').readline()
line = line.replace('O', 'A').replace('C', 'F').replace('D', 'F')
c = 1
ans = 1
for i in range(0, len(line) - 2, 2):
    if line[i] + line[i + 1] == 'FA' == line[i + 2] + line[i + 3]:
        c += 1
        ans = max(c, ans)
    else:
        c = 1
c = 1
for i in range(1, len(line) - 2, 2):
    if line[i] + line[i + 1] == 'FA' == line[i + 2] + line[i + 3]:
        c += 1
        ans = max(c, ans)
    else:
        c = 1
print(ans)
