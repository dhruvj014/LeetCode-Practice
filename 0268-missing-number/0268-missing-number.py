class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n*(n+1))/2
        checksum = 0
        for i in range(n):
            checksum += nums[i]
        return int(sum - checksum)