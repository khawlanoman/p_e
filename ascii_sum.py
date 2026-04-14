
def ascii_sum(word):
    count = 0
    for i in word:
        count = ord(i)
    return count

def sort_words_by_ascii(words):
    return(sorted(words, key=lambda word: (ascii_sum(word), len(word)), reverse= True))

words = ["Cat", "dog", "!"]
print(sort_words_by_ascii(words))
# ["dog", "Cat", "!"]
# because sums are: dog=314, Cat=280, !=33

words2 = ["", "A", " "]
print(sort_words_by_ascii(words2))
# ["A", " ", ""]
# sums: "A"=65, " "=32, ""=0