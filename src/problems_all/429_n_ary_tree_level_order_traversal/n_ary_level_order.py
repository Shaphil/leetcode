"""
Runtime:            58 ms
Beats:              6.58%
Memory:             19.33 MB
Beats:              12.49%
Submission:         https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/1511877263/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #tree, #bfs
Solved By:          #bfs
"""

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []  # Initialize with empty list


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize queue with the root node

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):  # Process all nodes at the current level
                node = queue.popleft()
                level.append(node.val)

                # Enqueue all children of the current node
                for child in node.children:
                    queue.append(child)

            result.append(level)  # Append the current level to the result

        return result


def build_tree(values: List[Optional[int]]) -> Optional[Node]:
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        parent = queue.popleft()

        # Handle None values correctly
        for _ in range(num_children(values, i)):
            if i < len(values) and values[i] is not None:
                child = Node(values[i])
                parent.children.append(child)
                queue.append(child)
            i += 1

    return root


def num_children(values: List[Optional[int]], i: int) -> int:
    """
    Helper function to determine the number of children for the current node.
    """
    num_children = 0
    while i < len(values) and values[i] is not None:
        num_children += 1
        i += 1
    return num_children


if __name__ == '__main__':
    arr = [1, None, 3, 2, 4, None, 5, 6]
    root = build_tree(arr)
    result = Solution().levelOrder(root)
    print(result)
