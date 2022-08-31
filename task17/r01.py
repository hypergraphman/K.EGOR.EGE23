count = 0
mx = 0
for i in range(1016, 7937 + 1):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        count += 1
        if mx < i:
            mx = i
print(count, mx)