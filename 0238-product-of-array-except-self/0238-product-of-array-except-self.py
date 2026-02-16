class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1]
        for i in range(1,len(nums)):
            sol.append(sol[i-1]*nums[i-1])
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            if i+1<len(nums):
                suff = suff*nums[i+1]            
            sol[i] = sol[i]*suff
        return sol