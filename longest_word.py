def longest_word(s):
    d=s.split(" ")
    max = d[0]
    for i in d:
        if len(i) > len(max):
            max = i

    return max

print(longest_word("The quick brown fox"))
# "quick"  ("quick" and "brown" are both length 5, return the first one)

print(longest_word("Boot dev makes coding fun"))
# "coding"

print(longest_word(""))
# ""  (no words)