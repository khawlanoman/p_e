
def unique_chars(word):
    word_set = set(word.lower())

    return (len(word_set))


def sort_words(words):
    return(sorted(words, key= lambda word:(unique_chars(word), word.swapcase())))

words = ["aaa", "abc", "AaA"]
print(sort_words(words))
# ["aaa", "AaA", "abc"]
# "aaa" and "AaA" each have 1 unique character (a), so they come before "abc" (3 unique characters).

words2 = ["ab", "aabb", "AB", "xyz", "x"]
print(sort_words(words2))
# ["x", "aabb", "ab", "AB", "xyz"]
# unique counts (case-insensitive):
# "x" -> 1
# "aabb", "ab", "AB" -> 2
# "xyz" -> 3
# For the words with 2 unique chars, the longer word "aabb" comes first.
