
def reverse_words(string:str):
    tab=[]
    list_jo=""
    tab = string.split(" ")
    """for i in tab[::-1]:
        list_jo += str(i)
        list_jo += " "
    """
    list_jo = " ".join(tab[::-1])
    return list_jo

sentence = "Hello World Python"
print(reverse_words(sentence))
# "Python World Hello"

sentence = "one two three"
print(reverse_words(sentence))
# "three two one"