class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for x in strs:                      
            p="".join(sorted(x))            
            
            if p not in dct:
                dct[p] = [x]
            else:
                dct[p].append(x)
                      
        return dct.values()