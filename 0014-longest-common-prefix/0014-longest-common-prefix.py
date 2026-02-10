class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        for i in range(len(first)):
            curr = first[i]
            for s in range(1,len(strs)):
                if i<len(strs[s]) and curr == strs[s][i]:
                    continue
                return prefix
            prefix += curr
        return prefix
