class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        ctr = 0
        n = ans
        while(n>1):
            ctr += n&1
            n = n >> 1
        if n == 1:
            ctr+=1
        return ctr