class Solution(object):
    def isValid(self, s):
        pastParens = []
        for i in range(len(s)):
            if self.isOpenParen(s[i]):
                pastParens.append(s[i])
            else:
                if len(pastParens) == 0:
                    return False
                op = pastParens.pop()
                cl = s[i]
                isValid = self.parenIsSameType(op,cl)
                if not isValid:
                    return False
        return len(pastParens) == 0


    def isOpenParen(self,p):
        if p =='(' or p =='[' or p == '{':
            return True
        else:
            return False

    def parenIsSameType(self, op, cl):
        if op == '(' and cl == ')':
            return True
        elif op == '{' and cl == '}':
            return True
        elif op == '[' and cl == ']':
            return True
        else:
            return False

s = Solution()
s.isValid("(amiraj)")