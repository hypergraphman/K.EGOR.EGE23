line = open('24-1.txt').readline()
line2 = ''
for el in line:
    if '0' <= el <= '9':
        line2 += el
    else:
        line2 += ' '
print(max(map(int, line2.split()), key=lambda x: x % 2 == 0))