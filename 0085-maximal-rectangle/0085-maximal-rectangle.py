class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        area = 0
        for i in range(len(heights)):
            while (len(st)>0 and heights[st[-1]]>heights[i]):
                el = st[-1]
                st.pop()
                nse = i
                pse = -1 if len(st) == 0 else st[-1]
                area = max(heights[el]*(nse-pse-1),area)
            st.append(i)
        while (len(st)>0):
            nse = len(heights)
            el = st[-1]
            st.pop()
            pse = -1 if len(st) == 0 else st[-1]
            area = max(heights[el]*(nse-pse-1),area)
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        maxArea = 0
        psum = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            totsum = 0
            for i in range(n):
                totsum += int(matrix[i][j])
                if(matrix[i][j] == "0"):
                    totsum = 0
                psum[i][j] = totsum
        for i in range(n):
            calc = self.largestRectangleArea(psum[i])
            maxArea = max(maxArea,calc)
        return maxArea