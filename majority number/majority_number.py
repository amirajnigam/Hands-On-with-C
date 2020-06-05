class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        l = len(nums)//2
        
        dic = {}
        
        for i in nums:
            dic[i] = 0
        
        for j in nums:
            if j in dic:
                dic[j] = dic[j] + 1
        
        for key, value in dic.items():
            if value > l:
                return(key)