def rotate_list(lst,k):
    if k == 0 or len(lst) == 0:
        return lst
    elif k == len(lst):
        return lst
   
    k = k % len(lst)


    return lst[-k:]  + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([10, 20, 30, 40], 4))
print(rotate_list([7, 8, 9], 5))
print(rotate_list([], 3))