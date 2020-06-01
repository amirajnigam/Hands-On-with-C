class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans = 0
        mini = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            
            else:
                ans = max(ans, prices[i] - mini)
        
        return ans          
            
# my code running individual test cases but run time error when submitted

#         N = len(prices)
        
#         l = min(prices)
#         k = prices.index(l)
        
#         new = []
#         for j in range(k, N):
#             new.append(prices[j])
#         if not new:
#             return 0
#         h = max(new)
#         result = (h - l)
#         return(result)