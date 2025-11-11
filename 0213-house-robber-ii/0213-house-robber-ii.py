class Solution:
    def house_robber_1(self, a,b,nums):
        n = len(nums)
        prev2 = nums[0] if a == 0 else 0
        prev = max(prev2,nums[1])
        for i in range(2,b+1):
            curr = max(prev,prev2+nums[i])
            prev2 = prev
            prev = curr
        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        calc1 = self.house_robber_1(0,n-2,nums)
        calc2 = self.house_robber_1(1,n-1,nums)
        return max(calc1,calc2)