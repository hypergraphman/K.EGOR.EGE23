line = open('24-12.txt').readline()
cur_len = 1
max_len = 1
for i in range(len(line) - 1):
    if line[i] <= line[i + 1]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 1

print(max_len)