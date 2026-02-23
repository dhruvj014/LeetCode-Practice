class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        longest = 0
        l,r = 0,0
        while r<len(s):
            curr = r - l
            if s[r] in checker:
                longest = max(longest,curr)
                while s[r] in checker:
                    checker.remove(s[l])
                    l+=1
            else:
                checker.add(s[r])
                r+=1
                curr+=1
                longest = max(longest,curr)            
        return longest