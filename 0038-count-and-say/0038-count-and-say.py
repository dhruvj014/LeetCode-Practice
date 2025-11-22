class Solution:
    def countAndSay(self, n: int) -> str:
        def recur(n):
            if n == 1:
                return "1"
            num = recur(n-1)
            base = num[0]
            ctr = 1
            newnum = ""
            if len(num)>1:
                for i in range(1,len(num)):
                    if num[i] == base:
                        ctr+=1
                        continue
                    else:
                        newnum+= str(ctr) + str(base)
                        base = num[i]
                        ctr = 1
            newnum+= str(ctr) + str(base)
            return newnum
        return recur(n)