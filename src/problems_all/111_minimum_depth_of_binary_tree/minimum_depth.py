"""
Runtime:            31 ms
Beats:              67.65%
Memory:             50.39 MB
Beats:              21.78%
Submission:         https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/1508455372/
Time complexity:    O(n)
Space complexity:   O(h) avg, where `h` = tree height, O(n) worst
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #dfs
"""

from collections import deque
from typing import Optional, List


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

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == '__main__':
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree(arr)
    result = Solution().minDepth(root)
    print(result)
