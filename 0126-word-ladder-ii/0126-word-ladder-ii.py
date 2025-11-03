class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # Step 1: BFS to build graph of shortest connections
        parents = defaultdict(set)
        distance = {beginWord: 0}
        q = deque([beginWord])
        found = False
        L = len(beginWord)

        while q and not found:
            level_visited = set()
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(L):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word not in word_set:
                            continue
                        if new_word not in distance:
                            distance[new_word] = distance[word] + 1
                            q.append(new_word)
                            level_visited.add(new_word)
                        if distance[new_word] == distance[word] + 1:
                            parents[new_word].add(word)
                        if new_word == endWord:
                            found = True
            word_set -= level_visited

        if not found:
            return []

        # Step 2: Backtrack from endWord to beginWord
        res = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return res