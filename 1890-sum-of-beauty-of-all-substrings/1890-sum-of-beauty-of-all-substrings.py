class Solution:
    def beautySum(self, s: str) -> int:
        sol = 0
        n = len(s)
        for i in range(n):
            freq = [0]*26
            for j in range(i,n):
                index = ord(s[j])-ord('a')
                freq[index] += 1

                maxfreq = 0
                minfreq = float('inf')
                for f in freq:
                    if f>0:
                        maxfreq = max(maxfreq,f)
                        minfreq = min(minfreq,f)
                sol+=maxfreq - minfreq
        return sol