
def vowel_count(word:str):
    count = 0
    for i in word:
        if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
            count +=1
    return(count)

def sort_words(list_word:list):
    return(sorted(list_word, key= lambda word: (len(word),word.lower(),word.swapcase(), vowel_count(word))))

words = [
    "apple",
    "Banana",
    "kiwi",
    "Apricot",
    "grape",
    "PEAR",
    "plum",
    "Orange",
    "fig",
    "Mango",
]

print(sort_words(words))