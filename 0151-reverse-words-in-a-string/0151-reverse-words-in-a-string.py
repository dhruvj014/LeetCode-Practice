class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        w = ""
        for i in range(len(s)-1,-1,-1):
            if(s[i]==" "):
                if(len(w)!=0):
                    if(len(ans)==0):
                        ans = w 
                    else:
                        ans = ans + " " + w
                    w = ""
            else:
                w = s[i] + w
        if len(w) != 0:
            if len(ans) == 0:
                ans = w
            else:
                ans += " " + w
        return ans