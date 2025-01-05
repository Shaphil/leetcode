"""
Runtime:            50 ms
Beats:              31.87%
Memory:             19.91 MB
Beats:              12.13%
Submission:         https://leetcode.com/problems/linked-list-cycle/submissions/1498695102/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #linked-list, #two-pointers, #hash-table
Solved By:          #linked-list
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        rabbit = head

        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next

            if rabbit == tortoise:
                return True

        return False


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    result = Solution().hasCycle(head)
    print(result)
