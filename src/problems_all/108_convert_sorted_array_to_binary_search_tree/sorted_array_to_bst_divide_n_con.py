"""
Runtime:    0 ms
Beats:      100.00%
Memory:     18.62 MB
Beats:      5.65%
Submission: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1466734874/
Topics:     #array, #divide-and-conquer, #tree, #binary-search-tree, #binary-tree
Solved By:  #divide-and-conquer
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


def print_bst(root):
    if not root:
        return ["null"]

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        else:
            result.append("null")

    return result


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    result = Solution().sortedArrayToBST(nums)
    res = print_bst(result)
    print(res)
