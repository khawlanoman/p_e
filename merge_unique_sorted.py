def merge_unique_sorted(list_1, list_2):
   new_list = sorted(set(list_1+list_2))

   return new_list

print(merge_unique_sorted([1, 3, 5], [2, 3, 4]))
# [1, 2, 3, 4, 5]

print(merge_unique_sorted([1, 1, 2], [2, 3, 3]))
# [1, 2, 3]

print(merge_unique_sorted([], [5, 1, 5]))
# [1, 5]