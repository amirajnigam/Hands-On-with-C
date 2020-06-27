class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        new = []
        
        for i in nums:
            new.append(i)
        new.sort()
               
        if nums == new:
            return 0
            
        for i in range(len(nums)):
            if nums[i] != new[i]:
                min = i
                break
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j] != new[j]:
                max = j
                break
            
        return ((max - min) + 1)