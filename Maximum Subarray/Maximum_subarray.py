 def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum = sum + nums[j]
                if sum >= max:
                    max = sum
                else:
                    pass
        return max