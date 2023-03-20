n, *a = map(int, open('27-53b.txt').read().split())
min1 = sorted(filter(lambda x: x % 3 == 1, a))
min2 = sorted(filter(lambda x: x % 3 == 2, a))
min0 = sorted(filter(lambda x: x % 3 == 0, a))
print(min1[:3])
print(min2[:3])
print(min0[:3])

# print(sum(min2[:3]))
# 963
print(min1[0] + min2[0] + min0[0])