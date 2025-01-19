"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.83 MB
Beats:              26.79%
Submission:         https://leetcode.com/problems/cousins-in-binary-tree/submissions/1513649515/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #bfs
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue = deque([(root, None)])

        while queue:
            level_size = len(queue)
            x_parent = y_parent = None

            for _ in range(level_size):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False

        return False


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


if __name__ == '__main__':
    arr = [1, 2, 3, None, 4, None, 5]
    x = 5
    y = 4
    root = build_tree(arr)
    result = Solution().isCousins(root, x, y)
    print(result)
