
def is_valid(word):
    stack=[]
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    for k in word:
        
        if k in pairs.values():
                stack.append(k)
        elif k in pairs:
            if not stack or stack.pop() != pairs[k]:
                return False

    return True

    


print(is_valid("()"))
# True

print(is_valid("()[]{}"))
# True

print(is_valid("(]"))
# False

print(is_valid("[()]"))


print(is_valid(")("))
print(is_valid("(eweqff)"))
# True