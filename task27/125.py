f = open('27-125a.txt')
n = int(f.readline())
a = list(map(int, f.readlines()))
ans = []
for i in range(n):
    right = i
    sum_r = a[right]
    left = i - 1
    sum_l = a[left]
    while abs(right % n - left % n) != 1 or right == i:
        if sum_r < sum_l:
            right += 1
            sum_r += a[right % n]
        else:
            left -= 1
            sum_l += a[left % n]
    ans.append((max(sum_r, sum_l), abs(i - right)))
print(min(ans))