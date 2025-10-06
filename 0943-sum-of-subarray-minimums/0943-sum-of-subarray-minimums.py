class Solution:
    def findNSE(self,arr:List[int]):
        n = len(arr)
        nse = [0]*n
        st = []
        for i in range(n-1,-1,-1):
            while(len(st)!=0 and arr[st[-1]]>=arr[i]):
                st.pop()
            nse[i] = n if len(st) == 0 else st[-1]
            st.append(i)
        return nse

    def findPSEE(self,arr:List[int]):
        n = len(arr)
        psee = [0]*n
        st = []
        for i in range(n):
            while(len(st)!=0 and arr[st[-1]]>arr[i]):
                st.pop()
            psee[i] = -1 if len(st) == 0 else st[-1]
            st.append(i)
        return psee
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.findNSE(arr)
        pse = self.findPSEE(arr)
        total = 0
        n = len(arr)
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            MOD = 10**9 + 7
            total = (total + (right*left*arr[i])% MOD)% MOD
        return total