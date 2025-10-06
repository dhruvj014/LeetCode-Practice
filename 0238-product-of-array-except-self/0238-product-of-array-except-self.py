class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = [1]*n
        pref = [1]*n
        prod = 1
        for i in range(1,n):
            prod = prod*nums[i-1]
            pref[i] = prod
        suff = [1]*n
        prod = 1
        for i in range(n-2,-1,-1):
            prod = prod*nums[i+1]
            suff[i] = prod
        
        for i in range(n):
            sol[i] = pref[i]*suff[i]
        return sol