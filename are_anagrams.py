def are_anagrams(s1,s2):
    count = 0
    s1=s1.replace(" ","")
    s2=s2.replace(" ","")
    
    for i in s1.lower():
        for k in s2.lower():
            if i == k:
                count +=1
                break
    if len(s1) != count or len(s1)!=len(s2):
        return False
    
    return True

print(are_anagrams("listen", "silent"))        # True
print(are_anagrams("Dormitory", "Dirty room"))  # True
print(are_anagrams("Conversation", "Voices rant on") ) # True

print(are_anagrams("hello", "world") )  # False
print(are_anagrams("test", "taste")  )  # False