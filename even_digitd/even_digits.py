class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for i in range(len(nums)):
            m = str(nums[i])
            N= len(m)
            if N%2 == 0:
                count += 1
            
        return(count)