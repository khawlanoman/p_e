
def char_frequency(s):
    d = {}
    for i in s:
        count = 0;
        for k in s:
            if k == i:
                count += 1
        d[i]= count

    return (d)
print(char_frequency("hello"))
# {"h": 1, "e": 1, "l": 2, "o": 1}

print(char_frequency("aaa"))
# {"a": 3}

print(char_frequency("abc"))
# {"a": 1, "b": 1, "c": 1}