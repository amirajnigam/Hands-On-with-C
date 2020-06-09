class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        snum = set(nums)
        
        for x in range(1,len(nums) + 1):   #index
            if x not in snum:
                res.append(x)
        
        return res
        
#alternate
        
#         missing = []
        
#         for i in nums:
#             pos = abs(i) - 1
#             if nums[pos] > 0:
#                 nums[pos] *= -1
        
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 missing.append(i+1)
        
#         return missing