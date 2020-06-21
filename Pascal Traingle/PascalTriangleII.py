class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # if rowIndex   == 0: return []
        
        if rowIndex == 0: return [1]
        
        Tri = [[1]]
        
        for i in range(1,rowIndex+1):
            row = [1]
            for j in range(1,i):
                row.append(Tri[i-1][j-1] + Tri[i-1][j]) 
            row.append(1)
            Tri.append(row)
    
        return Tri[rowIndex]