def remove_every_nth(lst,k):
    new_list=[]
    for idx,i in enumerate(lst):
        if isinstance(i,int):
            if i % k != 0:
                new_list.append(i)
        if isinstance(i, str):
             if idx != k -1 :
                new_list.append(i)
    return new_list
numbers = [1, 2, 3, 4, 5, 6]
print(remove_every_nth(numbers, 2))
# [1, 3, 5]
# (removes positions 2, 4, 6)

letters = ["a", "b", "c", "d", "e"]
print(remove_every_nth(letters, 3))
# ["a", "b", "d", "e"]
# (removes position 3)
print(remove_every_nth([10, 20, 30], 1))
# []  (removes every element)

print(remove_every_nth([1, 2, 3, 4], 10))
# [1, 2, 3, 4]  (n is larger than the list length)