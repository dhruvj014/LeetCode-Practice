import sys

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hasher = {}
        
        for i, num in enumerate(nums):
            if num not in hasher:
                hasher[num] = [1, i, i]  # freq, first, last
            else:
                hasher[num][0] += 1
                hasher[num][2] = i

        maxfreq = 0
        minlength = sys.maxsize

        for freq, first, last in hasher.values():
            if freq > maxfreq:
                maxfreq = freq
                minlength = last - first + 1
            elif freq == maxfreq:
                minlength = min(minlength, last - first + 1)

        return minlength