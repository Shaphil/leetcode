"""
https://leetcode.com/problems/middle-of-the-linked-list/


Runtime: 54 ms
Memory: 13.9 MB
https://leetcode.com/problems/middle-of-the-linked-list/submissions/870564963/
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, head: ListNode) -> int:
        _len = 0
        current = head

        while current is not None:
            _len += 1
            current = current.next

        return _len

    def getNode(self, head: ListNode, count: int) -> Optional[ListNode]:
        current = head
        for _ in range(count):
            current = current.next

        return current

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        _len = self.length(head)
        mid = _len // 2

        return self.getNode(head, mid)


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    result = Solution().middleNode(head)
    print(result.val)


if __name__ == '__main__':
    main()
