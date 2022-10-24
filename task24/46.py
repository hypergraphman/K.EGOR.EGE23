line = open('k7-m21.txt').readline()
index = 0
k = 0
for i in range(len(line) - 2):
    if line[i] < line[i + 1] < line[i + 2]:
        index = i
        k += 1
print(k, index)
