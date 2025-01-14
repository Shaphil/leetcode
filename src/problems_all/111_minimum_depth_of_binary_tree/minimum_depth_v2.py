"""
Runtime:            0 ms
Beats:              100.00%
Memory:             49.94 MB
Beats:              46.60%
Submission:         https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/1508464444/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #bfs
"""

from collections import deque
from typing import Optional


def build_tree(values):
    """
    Builds a binary tree from a list of values.
    None represents a null node.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    nodes = [root]
    i = 1
    while i < len(values):
        for node in nodes:
            if node:
                if i < len(values) and values[i] is not None:
                    node.left = TreeNode(values[i])
                    nodes.append(node.left)
                i += 1
                if i < len(values) and values[i] is not None:
                    node.right = TreeNode(values[i])
                    nodes.append(node.right)
                i += 1
    return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])  # (node, depth)
        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


if __name__ == '__main__':
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree(arr)
    result = Solution().minDepth(root)
    print(result)
