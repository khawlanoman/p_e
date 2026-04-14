def find_peak_index(nums):

    if len(nums) ==  1:
        return 0
    if  not nums:
        return -1
    for i in range(len(nums)):
        if i == 0:
            if len(nums)== 1 or nums[i] > nums[i+ 1]:
                return i
        elif i == len(nums) - 1:
            if nums[i] > nums[i - 1]:
                return i
        else:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

nums = [1, 1, 1, 6]
print(find_peak_index(nums))

nums = [1, 2, 3, 1]
print(find_peak_index(nums))

nums = [4]
print(find_peak_index(nums))


nums = []
print(find_peak_index(nums))

