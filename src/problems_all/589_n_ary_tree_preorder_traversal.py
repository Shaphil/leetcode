"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Runtime: 48 ms
Memory: 16.4 MB
"""


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def __init__(self) -> None:
        self.pre = []

    def preorder(self, root: Node) -> List[int]:
        if root:
            self.pre.append(root.val)
            if root.children:
                for child in root.children:
                    self.preorder(child)

        return self.pre


def main():
    tree = Node(1)
    children_level_1 = [Node(3), Node(2), Node(4)]
    children_level_2 = [Node(5), Node(6)]
    tree.children = children_level_1
    tree.children[0].children = children_level_2

    result = Solution().preorder(tree)
    print(result)


if __name__ == '__main__':
    main()
