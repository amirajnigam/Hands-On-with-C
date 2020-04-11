class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            dict[i] = 1
        
        count = 0
        for x in arr:
            if x + 1 in dict:
                count += 1
        
        return count