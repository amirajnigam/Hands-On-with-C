class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #[ 42,42,43]
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
        return False
    
    #alternate
    # if len(num_set) != len(nums)
    #     return  True
    # return False