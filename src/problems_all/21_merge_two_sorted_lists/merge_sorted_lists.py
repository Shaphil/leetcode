"""
Runtime:            36 ms
Beats:              5.32%
Memory:             13.10 MB
Beats:              100.00%
Submission:         https://leetcode.com/problems/merge-two-sorted-lists/submissions/239955915/
Time complexity:    O(n + m)
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
        elif l1 and not l2:
            return l1
        elif l2 and not l2:
            return l2

        root = ListNode(0)
        current = root
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    current.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    current.next = ListNode(l1.val)
                    l1 = l1.next

                current = current.next
            elif l1 and not l2:
                current.next = ListNode(l1.val)
                l1 = l1.next
                current = current.next
            elif l2 and not l1:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next

        current = root.next
        return current


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
