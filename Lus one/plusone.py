class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = [str(x) for x in digits]
        new_string = "".join(string)
        new_int = int(new_string)
        new_int += 1
        res = list(map(int,str(new_int)))
        return res