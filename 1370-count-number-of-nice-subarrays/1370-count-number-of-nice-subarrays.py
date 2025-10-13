class Solution:
    def atMost(self, nums, k):
        if k < 0:
            return 0
        left = 0
        total = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]%2
            while curr_sum > k:
                curr_sum -= nums[left]%2
                left += 1
            total += (right - left + 1)
        return total

    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums,goal) - self.atMost(nums,goal-1)