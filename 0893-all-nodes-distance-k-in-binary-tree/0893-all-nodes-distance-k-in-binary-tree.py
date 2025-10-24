# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []

        # Step 1: Build a map of each node's parent
        parent_map = {}
        self.map_parents(root, parent_map)

        # Step 2: Run BFS from the target node to find all nodes at distance K
        return self.bfs_from_target(target, parent_map, k)

    # This method builds a mapping of each node to its parent using BFS
    def map_parents(self, root: TreeNode, parent_map: dict):
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            # If left child exists, record its parent and add it to the queue
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            # If right child exists, record its parent and add it to the queue
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    # This method performs BFS starting from the target node to find nodes at distance K
    def bfs_from_target(self, target: TreeNode, parent_map: dict, k: int) -> List[int]:
        queue = deque()
        visited = set()

        queue.append(target)
        visited.add(target)

        current_level = 0

        # Standard BFS loop
        while queue:
            if current_level == k:
                break

            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()

                # Check left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                # Check right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                # Check parent node
                # If the parent exists and hasn't been visited, add it to the queue
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])

            current_level += 1

        return [node.val for node in queue]
        