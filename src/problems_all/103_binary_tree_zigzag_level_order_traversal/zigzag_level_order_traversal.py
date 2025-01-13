"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.86 MB
Beats:              42.19%
Submission:         https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1507675074/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #tree, #bfs, #binary-tree
Solved By:          #bfs
"""

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        is_zigzag = False

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                if is_zigzag:
                    level.insert(0, node.val)  # Add value to the front for zigzag
                else:
                    level.append(node.val)  # Add value to the end for normal order

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            is_zigzag = not is_zigzag

        return result


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
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree(arr)
    result = Solution().zigzagLevelOrder(root)
    print(result)
