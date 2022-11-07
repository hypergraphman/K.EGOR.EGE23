import re

c = 0
for i in range(1001385, 10**9*2, 2023):
    n = str(i)
    d1 = n[0] == '1'
    d2 = n[1] in '0123456789'
    d3 = n[2:5] == '493'
    d4 = n[-2:] == '41'
    if d1 and d2 and d3 and d4:
    # if re.fullmatch(r'1\d493\d*41', str(i)):
        print(i)
        c += 1
print(c)