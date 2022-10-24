line = open('24-1.txt').readline()
line2 = ''
for el in line:
    if '0' <= el <= '9':
        line2 += el
    else:
        line2 += ' '
print(max(filter(lambda x: x % 2 == 0, map(int, line2.split()))))
