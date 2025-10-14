class Solution:
    def atMostK(self, nums, K):
        freq = {}
        left = 0
        count = 0
        # Traverse the array with right pointer
        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                K -= 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Shrink the window if K becomes negative
            while K < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    K += 1
                left += 1
            count += (right - left + 1)
        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)