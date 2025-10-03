class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorall = 0
        for i in range(len(nums)):
            xorall = xorall ^ nums[i]
        rightmost = (xorall & (xorall-1)) ^ xorall
        b1 = 0
        b2 = 0
        for i in range(len(nums)):
            if(nums[i]&rightmost):
                b1 = b1 ^ nums[i]
            else:
                b2 = b2 ^ nums[i]
        return [b1,b2]