
def is_valid_with_depth(s, max_depth):
    stack=[]
    count = 0

    p ={
        ")":"(",
        "}":"{",
        "]":"["
    }

    for k in s:
        if k in p.values():
            stack.append(k)
        elif k in p:
            if not stack or stack[-1] != p[k]:
                return (False, "(not properly nested)")
            stack.pop()
    if stack:
        return (False, "(not properly nested)")

    for i in s:
        if i in p.values():
            count +=1
        elif i in p.keys():
            break

    if count != max_depth:
        return (False, f"(balanced, but max depth = {count} > limit {max_depth})")
    
    return (True, f"(balanced, max depth = {max_depth}, limit = {count})")


print(is_valid_with_depth("((()))", 3))
# True  (balanced, max depth = 3, limit = 3)

print(is_valid_with_depth("((()))", 2))
# False (balanced, but max depth = 3 > limit 2)

print(is_valid_with_depth("()[]{}", 1))
# True  (balanced, max depth = 1, limit = 1)

print(is_valid_with_depth("([{}])", 2))
# False (balanced, but max depth = 3 > limit 2)

print(is_valid_with_depth("([{}])", 3))
# True  (balanced, max depth = 3, limit = 3)

print(is_valid_with_depth("([)]", 3))
# False (not properly nested)