class Solution:
    def lowerBound(self, temp: List[int], t:int):
        for i in range(len(temp)):
            if temp[i] == t:
                return i
            if temp[i] > t:
                return i

    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        temp.append(nums[0])
        n = len(nums)
        for i in range(1,n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                continue
            index = self.lowerBound(temp,nums[i])
            temp[index] = nums[i]
        return len(temp)