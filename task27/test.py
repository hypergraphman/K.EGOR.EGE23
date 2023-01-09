from time import time

n = 10**6
st = time()
for i in range(n):
    i += 1
    a = i
print(time() - st)