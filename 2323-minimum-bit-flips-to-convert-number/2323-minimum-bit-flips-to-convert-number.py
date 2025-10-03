class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        ctr = 0
        for i in range(31):
            if(n & (1<<i)):
                ctr += 1
        return ctr