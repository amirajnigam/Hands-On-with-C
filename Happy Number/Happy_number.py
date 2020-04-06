class Solution:
    def isHappy(self, n: int) -> bool:
        def sqnums(nums):          
            result = 0
            while nums > 0:    
                mod = nums%10          
                nums = nums//10         
                result += mod*mod  
            return result                    
        seen =set()                       
        while sqnums(n) not in seen: 
            sum1 = sqnums(n)         
            if sum1 == 1:           
                return True
            else:
                seen.add(sum1)        
                n = sum1            
        return False