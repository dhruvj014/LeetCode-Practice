class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(groupSize):
                card = first+i
                if freq[card] == 0:
                    return False
                freq[card] -= 1
                if freq[card] == 0 and card == minHeap[0]:
                    heapq.heappop(minHeap)
        return True