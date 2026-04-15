def is_valid_brackets_only(s1):
    d ={
        "}":"{",
        ")":"(",
        "]":"["
    }
    stack =[]
    for i in s1:
        if i in d.values():
            stack.append(i)
        elif i in d.keys():
            if not stack or stack[-1] != d[i]:
                return False
            stack.pop()
    if stack:
        return False
    
    return True

print(is_valid_brackets_only("()"))        # True
print(is_valid_brackets_only("(]"))        # False
print(is_valid_brackets_only("{[()]}"))    # True
print(is_valid_brackets_only("{[(])}"))    # False