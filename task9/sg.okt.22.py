lines = open('09.txt').readlines()
c = 0
for line in lines:
    nums = list(map(int, line.split()))
    s = 0
    for num in nums:
        s += nums.count(num)
    if s == 10:
        s1 = 0
        s2 = 0
        for num in nums:
            if nums.count(num) == 2:
                s1 += num
            else:
                s2 += num
        if s1 // 2 < s2:
            c += 1
print(c)