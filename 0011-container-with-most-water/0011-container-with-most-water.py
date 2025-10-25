class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            side = min(height[left],height[right])
            area = side * (right - left)
            maxarea = max(area,maxarea)
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return maxarea