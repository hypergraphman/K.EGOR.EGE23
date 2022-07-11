from itertools import permutations, product

alf = 'гекэ023'
all_words = product(alf, repeat=4)
filter_words = set()
for i, word in enumerate(all_words, 1):
    word = ''.join(word)
    if word == '0гег':
        print(i)