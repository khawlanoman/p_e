
def vowel_count(word:str):
    count = 0
    for i in  word:
        if i =="a" or i == "e" or i =="i" or i == "o" or i=="u":
                count +=1
    
    return count

def sort_words_by_vowels(list_word:list):
    sort_vowels = sorted(list_word, key=lambda word: (vowel_count(word),len(word),word.lower()))

    return sort_vowels

words = ["Sky", "Aeiou", "test", "Apple", "rhythm"]
result = sort_words_by_vowels(words)
print(result)
# ["sky", "rhythm", "test", "Apple", "aeiou"]words = ["sky", "aeiou", "test", "Apple", "rhythm"]
