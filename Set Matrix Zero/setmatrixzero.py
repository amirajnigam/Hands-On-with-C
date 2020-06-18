class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        w = len(matrix[0]) # no of col
        
        h = len(matrix) #no of rows
        
        row_mask, col_mask = 0,0
        
        
        #Step1 Set up masking for zero element
        
        for y in range(h):
            for x in range(w):
                
                if matrix[y][x] == 0:
                    row_mask |= (1<<y)
                    col_mask |= (1<<x)
                    
        #step 2 Clear by row mask and column row
        
        for y in range(h):
            for x in range(w):
                if row_mask & (1<<y) or col_mask & (1<<x):
                    matrix[y][x] = 0