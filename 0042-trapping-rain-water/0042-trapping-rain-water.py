class Solution:
    def trap(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        leftMax = nums[l]
        rightMax = nums[r]
        total = 0
        while l<r:
            if leftMax < rightMax:
                calc = leftMax - nums[l]
                if calc>0:
                    total += calc
                leftMax = max(leftMax, nums[l])
                if leftMax < rightMax:
                    l+=1
                else:
                    r-=1
            else:
                calc = rightMax - nums[r]
                if calc>0:
                    total += calc
                rightMax = max(rightMax, nums[r])
                if leftMax < rightMax:
                    l+=1
                else:
                    r-=1
        return total