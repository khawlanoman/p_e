def find_missing_number(s_list):
    new_list = sorted(s_list)
    found = 0
    max_l = max(new_list)
    min_l = min(new_list)
   
    for i in range(min_l,max_l):
        if i in new_list:
            continue
        else:
            found = i
    return found


nums = [1, 2, 4, 5]
print(find_missing_number(nums))
# 3  (range is 1..5)

nums = [2, 3, 1, 5]
print(find_missing_number(nums))
# 4  (range is 1..5)