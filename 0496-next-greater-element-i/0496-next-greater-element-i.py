class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = [0]*len(nums2)
        st = []
        for i in range(len(nums2)-1,-1,-1):
            while (len(st)>0) and st[-1]<= nums2[i]:
                st.pop()
            if len(st) == 0:
                res1[i] = -1
            else:
                res1[i] = st[-1]
            st.append(nums2[i])
        # return res1
        res = []
        for n in nums1:
            for i in range(len(nums2)):
                if n == nums2[i]:
                    res.append(res1[i])
                    break
        return res