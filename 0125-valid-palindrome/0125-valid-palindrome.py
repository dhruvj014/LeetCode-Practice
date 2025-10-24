class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if not s:
        #     return False
        left = 0
        right = len(s) - 1
        while(left < right):
            l = s[left]
            r = s[right]
            if not l.isalnum():
                left+=1
                continue
            if not r.isalnum():
                right-=1
                continue
            if l.isupper():
                l = l.lower()
            if r.isupper():
                r = r.lower()
            if l==r:
                left+=1
                right-=1
            else:
                return False
        return True