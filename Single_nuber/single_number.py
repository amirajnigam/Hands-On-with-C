def single_number(nums):

    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    return res
    
nums = [2,2,1]
print(single_number(nums))