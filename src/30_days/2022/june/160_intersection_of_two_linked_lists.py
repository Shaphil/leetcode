from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_len(self, head):
        count = 0
        while head:
            head = head.next
            count += 1

        return count

    def skip_nodes(self, head, skip_amount):
        for _ in range(skip_amount):
            head = head.next

        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena = self.get_len(headA)
        lenb = self.get_len(headB)

        if lena > lenb:
            headA = self.skip_nodes(headA, lena - lenb)
        elif lenb > lena:
            headB = self.skip_nodes(headB, lenb - lena)

        while headA:
            if headA is headB:
                return headB

            headA = headA.next
            headB = headB.next

        return None
