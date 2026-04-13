def most_frequent(s_list):
    d ={}

    for  i in s_list:
        count  = 0
        for k in s_list:
            if k== i:
                count +=1
        d[i]=count
    if d:
        max_d = list(d.values())[0]
        max_k = list(d.keys())[0]
    else:
        max_d = None
        max_k = None
   
    for key,value in d.items():
        if value > max_d:
            max_d = value
            max_k = key
    return max_k

print(most_frequent([1, 2, 2, 3, 3, 3]))
# 3

print(most_frequent([1, 1, 2, 2]))
# 1 or 2 (either is OK, both are most frequent)

print(most_frequent([5]))
# 5

print(most_frequent([]))
# None