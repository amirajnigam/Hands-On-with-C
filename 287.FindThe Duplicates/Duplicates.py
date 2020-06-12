class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#Method1 Tortoise and Hare algo(Flyod's)     
        tortoise = hare = nums[0]
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if tortoise == hare:
                break    
        tortoise = nums[0]
        while tortoise != hare:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return hare
    # T: O(n)
    # S: O(1)
        
        
# Method1 sort and scan       
#         nums.sort()
#         print(nums)
        
#         for i in range(len(nums)):
#             if nums[i+1] == nums[i]:
#                 return nums[i]
# T = O(nlogn)
# S = O(1)
# Issue: array modified
    
#  Method2: set
#         a = set()
#         for i in nums:
#             if i in a:
#                 return i
#             else:
#                 a.add(i)
# T = O(n)
# S = O(n)
# Issue = space not O(n)