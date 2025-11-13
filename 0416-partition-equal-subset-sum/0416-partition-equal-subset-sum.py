class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = 0
        for num in nums:
            total += num
        if total%2:
            return False
        target = int(total/2)
        dp = [False for _ in range(target+1)]
        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True
        for i in range(1,n):
            temp = [False for _ in range(target+1)]
            for j in range(1,target+1):
                take = dp[j - nums[i]] if j >= nums[i] else False
                not_take = (dp[j])
                temp[j] = take or not_take
            dp = temp
        return dp[target]