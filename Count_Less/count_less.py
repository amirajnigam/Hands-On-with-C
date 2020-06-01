class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        
        new = []
        i = j = 0 
        
        for i in range(N):
            count = 0 
            for j in range(N):
                if j != i and nums[j] < nums[i]:
                    count += 1
            new.append(count)
        return new