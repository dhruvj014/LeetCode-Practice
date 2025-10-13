class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = [-1,-1,-1]
        ctr = 0
        for i in range(len(s)):
            lastseen[ord(s[i]) - ord('a')] = i
            if(lastseen[0]!= -1 and lastseen[1]!= -1 and lastseen[2]!= -1):
                ctr = ctr + (1+min(lastseen[0],min(lastseen[1],lastseen[2])))
        return ctr