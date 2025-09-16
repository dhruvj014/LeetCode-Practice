class Solution:
    def maxDepth(self, s: str) -> int:
        ctr = 0
        max_ctr = 0
        for i in range(len(s)):
            if(s[i] == "("):
                ctr += 1
                max_ctr = max(max_ctr,ctr)
            elif(s[i] == ")"):
                ctr -= 1
        return max_ctr