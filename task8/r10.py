from itertools import permutations, product

alf = 'kapkan'
all_words = permutations(alf)
filter_words = set()
for word in all_words:
    word = ''.join(word)
    if 'kk' not in word and 'aa' not in word:
        filter_words.add(word)
print(filter_words)
print(len(filter_words))