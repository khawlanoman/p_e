def find_pairs_with_sum(nums,target):
    new_list = []

    for i in nums:
        tar1 = i
        for  k in nums:
            if  tar1 + k == target:
                new_list.append((tar1,k))
                break
    list_tar=[]
    for  i in new_list:
        list_tar.append(i[::-1])
    return new_list


nums = [1, 2, 3, 4]
target = 5
print(find_pairs_with_sum(nums, target))
# [(1, 4), (2, 3)]

nums = [0, -1, 2, -3, 1]
target = 1
print(find_pairs_with_sum(nums, target))
# [(0, 1), (-1, 2)]

nums = [2, 2, 3, 3]
target = 5
print(find_pairs_with_sum(nums, target))
# [(2, 3), (2, 3), (2, 3), (2, 3)]