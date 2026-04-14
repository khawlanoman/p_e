def filter_and_square_evens(s_list):
    """r_list = []
    for i in s_list:
        if i % 2 == 0:
            r_list.append(i*i)
    """
    

    r_list=[x * x for x in  s_list if x % 2== 0]

    return r_list
print(filter_and_square_evens([1, 2, 3, 4, 5, 6]))
# [4, 16, 36]

print(filter_and_square_evens([0, 1, 2, -2]))
# [0, 4, 4]

print(filter_and_square_evens([1, 3, 5]))
# []