class Solution:
    def trap(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],nums[i])
        suffixMax = [0]*n
        suffixMax[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffixMax[i] = max(suffixMax[i+1],nums[i])

        for i in range(n):
            leftMax = prefix[i]
            rightMax = suffixMax[i]
            if(nums[i]<leftMax and nums[i]<rightMax):
                total+= min(leftMax,rightMax) - nums[i]
        return total