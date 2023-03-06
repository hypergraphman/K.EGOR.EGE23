cubes = []
with open('26-sg.txt') as f:
    for line in f.readlines():
        x, y = line.split()
        cubes.append((int(x), y))
cubes.sort(reverse=True)
blocks = []
while cubes:
    block = [cubes.pop(0)]
    i = 0
    while i < len(cubes):
        if cubes[i][1] != block[-1][1] and block[-1][0] - cubes[i][0] >= 5:
            block.append(cubes.pop(i))
        else:
            i += 1
    blocks.append(block)
print(max(len(x) for x in blocks), len(blocks))
