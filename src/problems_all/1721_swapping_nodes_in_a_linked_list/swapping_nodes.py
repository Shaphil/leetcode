"""
Runtime:            20 ms
Beats:              98.84%
Memory:             40.17 MB
Beats:              27.12%
Submission:         https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/1498916253/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #linked-list, #two-pointers
Solved By:          #linked-list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current)
            current = current.next

        temp = arr[k - 1].val
        arr[k - 1].val = arr[len(arr) - k].val
        arr[len(arr) - k].val = temp

        return arr[0]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2

    result = Solution().swapNodes(head, k)
    while result:
        print(result.val, end=", ")
        result = result.next
