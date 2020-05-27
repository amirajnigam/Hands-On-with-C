class Solution:
    def fib(self, N: int) -> int:
        #recursive method
        if N <= 1:
            return(N)
        else:
            return (self.fib(N-1) + self.fib(N-2))
        
        #iterative ethod using dict
        
        seen = {0:0, 1:1}
        
        for i in range(2, N+1):
            seen[i] = seen[i-1] + seen[i-2]
        
        return(seen[N])