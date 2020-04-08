class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_of_arr = nums[0]
        curr_arr = nums[0]
        
        for i in range(1, len(nums)):
            curr_arr = max(nums[i], curr_arr + nums[i])
            max_of_arr = max(curr_arr, max_of_arr)
        return max_of_arr