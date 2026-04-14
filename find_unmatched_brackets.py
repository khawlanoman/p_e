
def find_unmatched_brackets(string:str):
    stack=[]
    l_index=[]
    p = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for index, k in enumerate(string):
        if k in p.values():
            stack.append((k, index))
        elif k in p:
            if not stack or stack[-1][0] != p[k]:
                l_index.append(index)
            else:  
                stack.pop()
    #for _, ind in  stack:
     #   l_index.append(ind)
    l_index.extend (ind for _,ind in stack)

    return sorted(l_index)


s = "(()(()"
print(find_unmatched_brackets(s))
# [0, 3]
# '(' at index 0 and '(' at index 3 never get matched

s2 = "()[{}]"
print(find_unmatched_brackets(s2))
# []  (all brackets are matched and properly nested)

s3 = "a(b]c"
print(find_unmatched_brackets(s3))
# [1, 3]
# '(' at index 1 and ']' at index 3 are both unmatched
