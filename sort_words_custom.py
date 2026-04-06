def sort_words_custom(sort_word:list):
    sort =sorted(sort_word, key= lambda word : (len(word),word.lower(),word.swapcase()))
    return sort

words = ["Cat", "cat", "Dog", "dog"]
print(sort_words_custom(words))
# ["cat", "Cat", "dog", "Dog"]

words = ["a", "A", "aa", "AA", "b", "B"]
print(sort_words_custom(words))
# ["a", "A", "b", "B", "AA", "aa"]