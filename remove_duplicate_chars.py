
def remove_duplicate_chars(text:str):
    word = "".join(dict.fromkeys(text))
    return word

print(remove_duplicate_chars("aabbccabc")  ) # "abc"
print(remove_duplicate_chars("banana") )     # "ban"
print(remove_duplicate_chars("")    )       # ""
print(remove_duplicate_chars("aaaa") )      # "a"