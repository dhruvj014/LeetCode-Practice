class Solution:
    def checkValidString(self, s: str) -> bool:
        minval,maxval = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                minval += 1
                maxval += 1
            elif s[i] == ')':
                minval -= 1
                maxval -= 1
            else:
                minval -= 1
                maxval += 1
            if(minval < 0):
                minval = 0
            if(maxval < 0):
                return False
        return minval == 0