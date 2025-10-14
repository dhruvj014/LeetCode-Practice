class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hasher = [0] * 256
        n = len(s)
        m = len(t)
        l, r = 0, 0
        minlen = sys.maxsize
        sindex = -1
        ctr = 0

        for i in range(m):
            hasher[ord(t[i])] += 1

        while r < n:
            # Always reduce the count in the hasher
            hasher[ord(s[r])] -= 1
            if hasher[ord(s[r])] >= 0:
                ctr += 1

            while ctr == m:
                if (r - l + 1) < minlen:
                    minlen = r - l + 1
                    sindex = l
                hasher[ord(s[l])] += 1
                if hasher[ord(s[l])] > 0:
                    ctr -= 1
                l += 1

            r += 1

        if sindex == -1:
            return ""
        return s[sindex:sindex + minlen]