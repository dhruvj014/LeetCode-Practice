class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        stream = s+s
        if(len(s)!=len(goal)):
            return False
        if goal in stream:
            return True
        else:
            return False