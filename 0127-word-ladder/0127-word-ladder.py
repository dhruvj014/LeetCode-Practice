class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque([(beginWord,1)])
        word_set = set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    replaced_word = word[:i] + ch + word[i+1:]
                    if replaced_word in word_set:
                        word_set.remove(replaced_word)
                        q.append((replaced_word, steps + 1))
        return 0