 
def vowel_count(word):
    count = 0
    for i in word:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count +=1
    return count

def custom_ascii_key(word):
    list_ascii=[]
    for i in word:
        list_ascii.append(ord(i))
    return(list_ascii)

def sort_words_advanced(words:list):
    return(sorted(words,key= lambda word: (len(word), custom_ascii_key(word), vowel_count(word))))


words = ["", "a", "A", "TEST", "test", "Test"]
print(sort_words_advanced(words))