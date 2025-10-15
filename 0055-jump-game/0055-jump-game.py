class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mind = 0
        for i in range(len(nums)):
            if i>mind:
                return False
            mind = max(mind, i + nums[i])
        return True