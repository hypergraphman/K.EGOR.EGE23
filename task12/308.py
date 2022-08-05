line = '9' * 96
while '22222' in line or '9999' in line:
    if '22222' in line:
        line = line.replace('22222', '99', 1)
    else:
        line = line.replace('9999', '2', 1)

    print(line)