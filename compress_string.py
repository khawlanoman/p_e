def compress_string(s):
    str=""

    for i in s:
        count = 0
        for k in s:
            if k == i:
                count +=1
        if i in str:
            continue
        str+=i
        str+=chr(count + 48)

    if len(str) >= len(s):
        return s
    
    return str


print(compress_string("aaabbbcc"))
# "a3b3c2"

print(compress_string("aaa"))
# "a3"

print(compress_string("abc"))
# "abc" because "a1b1c1" is longer

print(compress_string("aabbcc"))
# "aabbcc" because "a2b2c2" is the same length
