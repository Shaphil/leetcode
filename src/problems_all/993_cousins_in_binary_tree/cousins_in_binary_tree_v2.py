"""
Runtime:            0 ms
Beats:              100.00%
Memory:             18.00 MB
Beats:              16.37%
Submission:         https://leetcode.com/problems/cousins-in-binary-tree/submissions/1513656005/
Time complexity:    O(n)
Space complexity:   O(h), where, `h` is the height of the tree
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #dfs
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
        def dfs(node, parent, depth, target, result):
            if not node:
                return

            if node.val == target:
                result.extend([parent, depth])
                return

            dfs(node.left, node, depth + 1, target, result)
            dfs(node.right, node, depth + 1, target, result)

        x_info, y_info = [], []
        dfs(root, None, 0, x, x_info)
        dfs(root, None, 0, y, y_info)

        return x_info[1] == y_info[1] and x_info[0] != y_info[0]


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
