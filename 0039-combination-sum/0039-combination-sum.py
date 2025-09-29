class Solution:
    def combinationSum(self, arr: List[int], x: int) -> List[List[int]]:
        n = len(arr)
        res = []
        st = []

        def backtrack(i,target,st):
            if i == n:
                if target == 0:
                    res.append(st[:])
                return
            if arr[i]<=target:
                st.append(arr[i])
                backtrack(i,target - arr[i],st)
                st.pop()
            backtrack(i+1,target,st)
        
        backtrack(0,x,st)
        return res
