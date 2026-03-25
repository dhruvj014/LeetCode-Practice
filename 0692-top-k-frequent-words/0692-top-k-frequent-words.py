class Solution:
    def topKFrequent(self, words, k):
        freq = Counter(words)
        
        return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]