class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i],0)
        sort_map = dict(sorted(hashmap.items(),key = lambda item:item[1], reverse = True))
        ans = ""
        for c in sort_map:
            ctr = sort_map[c]
            # print("Ctr - "+str(ctr))
            for i in range(ctr):
                ans += c
        return ans