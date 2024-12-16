"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.31 MB
Beats:              11.04%
Submission:         https://leetcode.com/problems/merge-two-sorted-lists/submissions/1480353241/
Time complexity:    O(min(n, m))
Space complexity:   O(1)
Topics:             #linked-list, #recursion
Solved By:          #linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append remaining elements from the non-empty list
        current.next = l1 if l1 else l2

        return dummy.next


if __name__ == '__main__':
    list1 = ListNode(x=1)
    list1.next = ListNode(x=2)
    list1.next.next = ListNode(x=4)

    list2 = ListNode(x=1)
    list2.next = ListNode(x=3)
    list2.next.next = ListNode(x=4)

    output = Solution().mergeTwoLists(list1, list2)
    while output:
        print(output.val, end=' ')
        output = output.next
