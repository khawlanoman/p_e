
def is_valid_brackets_only(string:str):
    stack=[]
    
    p = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for k in string:
        if k in p.values():
            stack.append(k)

        elif k in p:
            if not stack or stack[-1] != p[k]:
                return False
            stack.pop()
        elif k.isalpha():
            continue
    
    if stack:
        return False
    
    return True

print(is_valid_brackets_only("a(b)c"))
# True

print(is_valid_brackets_only("hello[world]"))
# True

print(is_valid_brackets_only("123{456}"))
# True

print(is_valid_brackets_only("([a)]"))
# False

print(is_valid_brackets_only("no brackets here"))
# True