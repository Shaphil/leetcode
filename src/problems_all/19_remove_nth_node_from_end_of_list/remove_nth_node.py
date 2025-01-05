"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.68 MB
Beats:              24.08%
Submission:         https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1498624475/
Time complexity:    O(L), where `L` is the length of the list
Space complexity:   O(1)
Topics:             #linked-list, #two-pointers
Solved By:          #linked-list
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node):
    head = []
    while node:
        head.append(node.val)
        node = node.next
    print(head)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head

        while current:
            current = current.next
            length += 1

        if n == length:
            return head.next

        current = head
        for _ in range(length - n - 1):
            current = current.next

        current.next = current.next.next

        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2

    result = Solution().removeNthFromEnd(head, n)
    print_list(result)
