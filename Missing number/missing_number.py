class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
        
        #my approach 92/122 test cases passed
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     N = nums[i+1] - nums[i]
        #     if N != 1:
        #         return(nums[i] + 1)
        