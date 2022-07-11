from itertools import permutations, product
from re import fullmatch

alf = '01234567'
all_words = product(alf, repeat=5)
filter_words = set()
for word in all_words:
    word = ''.join(word)
    if word.count('6') == 1 and word[0] != '0' and (fullmatch(r'\d*[024][6][024]\d*', word) or fullmatch(r'[6][024]\d*', word) or fullmatch(r'\d*[024][6]', word)):
        filter_words.add(word)
print(filter_words)
print(len(filter_words))