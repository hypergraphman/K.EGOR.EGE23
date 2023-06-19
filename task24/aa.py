s = open('test.txt').read()

cur_len = 1
mx_len = 0
for i in range(len(s) - 2):
    if s[i] == s[i + 1]:
        cur_len += 1
        if cur_len > mx_len:
            if s[i + 2] != s[i + 1] and s[i + 2] == s[i + 1 - cur_len]:
                mx_len = cur_len
    else:
        cur_len = 1
print(mx_len)