class Solution:
    def reverse(self, x: int) -> int:
        
        if x < -2147483648 or x > 2147483647:
            return 0
        if x < 0:
            sign = -1 
        else:
            sign = 1 
        x = abs(x)
        while x:
            if x % 10 == 0: 
                x //= 10
            else:
                break              
        y = str(x)
        lst = list(y)
        lst.reverse()
        x = "".join(lst)
        x = int(x)
        if x < -2147483648 or x > 2147483647:
            return 0
        return(sign * x)