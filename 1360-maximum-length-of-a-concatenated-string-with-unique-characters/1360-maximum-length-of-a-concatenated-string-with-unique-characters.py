class Solution:
    def maxLength(self, arr: List[str]) -> int:
        check = set()
        n = len(arr)
        ctr = 0
        def backtrack(index,word):
            if index == n:
                return len(word)
            ch = arr[index]
            if len(set(ch)) != len(ch):
                return backtrack(index+1,word)
            take = True
            for c in ch:
                if c in check:
                    take = False
                    break
            res = backtrack(index+1,word)
            if take:
                for c in ch:
                    check.add(c)
                res = max(res,backtrack(index+1,word+ch))
                for c in ch:
                    check.remove(c)
            return res
        return backtrack(0,"")