class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = 0
        moves = 0
        for i in range(len(s)):
            if s[i] == "(":
                st+=1
            else:
                if st==0:
                    moves+=1
                else:
                    st-=1
        return moves + st