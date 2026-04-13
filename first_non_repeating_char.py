def first_non_repeating_char(s):
    new_dic={}

    for k in s:
        count = 0
        for i in s:
            if k == i:
                count +=1
        new_dic[k]= count
    
    min_l = min(new_dic,key=new_dic.get)
    
    return min_l

s = "leetcode"
print(first_non_repeating_char(s))
# "l" (only "l" appears once, and it appears before any other unique character)

s = "aabbccdee"
print(first_non_repeating_char(s))
# "d" ("d" is the first character that appears once)

s = "aabb"
print(first_non_repeating_char(s))
# "" (empty string, because every character repeats)