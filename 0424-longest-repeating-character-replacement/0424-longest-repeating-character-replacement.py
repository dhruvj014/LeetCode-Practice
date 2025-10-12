class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxlen,maxf = 0,0,0,0
        hasher = [0]*26
        while(r<len(s)):
            hasher[ord(s[r])-ord('A')]+=1
            maxf = max(maxf, hasher[ord(s[r]) - ord('A')])
            if((r-l+1) - maxf > k):
                hasher[ord(s[l]) - ord('A')]-=1
                maxf = 0
                l+=1
            if((r-l+1)-maxf<=k):
                maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen