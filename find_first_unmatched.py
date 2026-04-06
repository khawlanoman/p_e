
def find_first_unmatched(string:str):
    stack = []
    p ={
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for index, k  in enumerate(string):
        
        if k in p.values():
            stack.append((k,index))
        elif k in p:
            if not stack or stack[-1][0] != p[k]:
                return index
            stack.pop()
    if stack:
        return stack[0][1]
    
    return (-1)

s = "(("
print(find_first_unmatched(s))
# 0  (the opening bracket at index 0 is never closed)

s = "(())"
print(find_first_unmatched(s))
# -1  (all brackets are balanced)

s = "()"
print(find_first_unmatched(s))
# -1  (balanced)

s = "([)]"
print(find_first_unmatched(s))
# 2  (the ')' at index 2 closes the wrong opening bracket)

s = ")(" 
print(find_first_unmatched(s))
# 0  (closing bracket at index 0 has no matching opening)