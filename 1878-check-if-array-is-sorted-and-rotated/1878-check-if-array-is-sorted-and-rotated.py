class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lenarr = len(nums)
        checker = 0
        for i in range(1,lenarr):
            if(nums[i]<nums[i-1]):
                checker+=1
            if(checker>=2):
                return False

        if(checker==0):
            return True

        if(nums[-1]<=nums[0]):
           return True
        else:
            return False
        
        