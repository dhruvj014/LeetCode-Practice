class Solution:
    def myAtoi(self, s: str) -> int:
        sol = []
        neg = False
        pos = False
        for i in range(len(s)):
            if(s[i]==" " and len(sol)==0 and pos==False and neg== False):
                continue
            elif(s[i] == "-" and len(sol)==0 and pos==False and neg==False):
                neg = True
            elif(s[i] == "+" and len(sol)==0 and neg==False and pos==False):
                pos = True
                continue
            elif(s[i].isdigit()):
                sol.append(s[i])
            else:
                break
        if(len(sol)==0):
            return 0
        num = int("".join(sol))
        if(neg):
            if(-(num)<((-2)**31)):
                return ((-2)**31)
            return (-num)
        else:
            if(num>(2**31)-1):
                return (2**31)-1
            return num