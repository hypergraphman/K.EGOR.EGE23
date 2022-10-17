line = open('24.txt').readline()
words = line.replace('O', 'A').replace('C', 'F').replace('D', 'F').replace('FA', '1').replace('F', 'A').split('A')
print(len(max(words, key=lambda x: len(x))))