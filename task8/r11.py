from itertools import permutations, product

alf = 'skola'
all_words = product(alf, repeat=3)
filter_words = set()
for word in all_words:
    word = ''.join(word)
    if word.count('k') == 1:
        filter_words.add(word)
print(filter_words)
print(len(filter_words))