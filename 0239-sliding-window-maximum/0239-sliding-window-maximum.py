from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        sol = []
        for i in range(n):
            if(q and q[0]==i-k):
                q.popleft()
            while(q and nums[q[-1]]<nums[i]):
                q.pop()
            q.append(i)
            if(i>=k-1):
                sol.append(nums[q[0]])
        return sol