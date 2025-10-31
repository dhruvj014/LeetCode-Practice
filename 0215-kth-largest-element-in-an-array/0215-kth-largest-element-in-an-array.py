class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, num)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        # print(maxHeap)
        # while k>0:
        #     sol = heapq.heappop(maxHeap)
        #     k-=1
        return heapq.heappop(maxHeap)