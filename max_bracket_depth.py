
def max_bracket_depth(string:str):
    stack = []
    check = 1
    count = 0
    p ={
        ")":"("
       }
    
    for k in string:
        if k in p.values():
            stack.append(k)
        elif k in p:
            if not stack or stack[-1] != p[k]:
                return -1
            stack.pop()
            
    if stack:
        return -1
    
    if check == 1:
        for i in string:
            if i == "(":
                count +=1
            elif i == ")":
                break
    
    
    return count


  


print(max_bracket_depth("((()))"))
# 3  (three levels deep)

print(max_bracket_depth("()()"))
# 1  (no nesting, just a single level each time)

print(max_bracket_depth("(())(())"))
# 2  (two levels deep in each group)

print(max_bracket_depth("())("))
# -1 (not balanced)

print(max_bracket_depth(""))
# 0  (empty string has depth 0)