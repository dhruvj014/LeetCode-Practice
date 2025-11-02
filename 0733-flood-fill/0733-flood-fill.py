class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = collections.deque()
        original = image[sr][sc]
        if original == color:
            return image
        image[sr][sc] = color
        q.append((sr,sc))
        # for r in range(len(image)):
        #     for c in range(len(image[0])):
        #         if image[r][c] == original and r!= sr and c != sc:
        #             q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(image))
                        and col in range(len(image[0]))
                        and image[row][col] == original
                    ):
                        image[row][col] = color
                        q.append((row, col))
        return image