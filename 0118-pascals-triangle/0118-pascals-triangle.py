class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]]
        if n == 1:
            return ans
        if n == 2:
            ans.append([1,1])
            return ans
        for i in range(2,n+1):
            new_row = [1]
            prev = ans[-1]
            for i in range(len(prev)-1):
                new_row.append(prev[i] + prev[i+1])
            new_row.append(1)
            ans.append(new_row)
        return ans