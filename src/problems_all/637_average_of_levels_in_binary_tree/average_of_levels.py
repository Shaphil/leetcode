"""
Runtime:            2 ms
Beats:              56.21%
Memory:             20.01 MB
Beats:              7.64%
Submission:         https://leetcode.com/problems/average-of-levels-in-binary-tree/submissions/1510576195/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #tree, #bfs, #dfs, #binary-tree
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total = sum(current_level)
            avg = total / len(current_level)
            result.append(avg)

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
    result = Solution().averageOfLevels(root)
    print(result)
