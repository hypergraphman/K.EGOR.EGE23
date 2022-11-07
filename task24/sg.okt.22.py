line = open('24.txt').readline()
line = line.replace('O', 'A').replace('C', 'F').replace('D', 'F')
line = line.replace('FFA', '1').replace('F', ' ').replace('A', ' ')
print(len(max(line.split())))
