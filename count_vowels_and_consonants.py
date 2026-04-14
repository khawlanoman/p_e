def count_vowels_and_consonants(s):
    count_v = 0
    count_c = 0
    for i in s.lower():
        if i.isalpha():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count_v +=1
            else:
                count_c +=1
                
    t = (count_v,count_c)
    return t

print(count_vowels_and_consonants("Hello, World! 123"))
# (3, 7)

print(count_vowels_and_consonants("Boot.dev"))
# (3, 4)
print(count_vowels_and_consonants(""))
# (3, 4)