class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
        hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i, key in enumerate(hashmap):
            if i < k:
                res.append(key[0])
            else:
                break
        return res