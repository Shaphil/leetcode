"""
https://leetcode.com/problems/evaluate-boolean-binary-tree/description/
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.vals = (0, 1)

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """Using recursive DFS"""

        if root.val in self.vals:
            return bool(root.val)
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
