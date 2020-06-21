class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:]  = nums[::-1]            #[7,6,5,4,3,2,1]
        nums[:k] = nums[:k][::-1]        #[5,6,7,4,3,2,1]
        nums[k:] = nums[k:][::-1]        #[5,6,7,1,2,3,4]
        
        
#         j = 1
#         for i in range(len(nums)):
#             while j <= k:
#                 a = nums.pop()
#                 nums.insert(0,a)
#                 j += 1
#         print(nums)
                
                