class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sumall = 0
        for i in range(len(s)):
            if(i+1<len(s) and mapper[s[i]]<mapper[s[i+1]]):
                sumall-=mapper[s[i]]
            else:
                sumall+=mapper[s[i]]
        return sumall