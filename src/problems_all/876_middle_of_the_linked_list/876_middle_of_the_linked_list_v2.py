"""
https://leetcode.com/problems/middle-of-the-linked-list/


Runtime: 32 ms
Memory: 13.7 MB
https://leetcode.com/problems/middle-of-the-linked-list/submissions/321604323/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        middle = length // 2
        counter = 0
        current = head
        while counter < middle:
            current = current.next
            counter += 1

        return current


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    result = Solution().middleNode(head)
    print(result.val)


if __name__ == '__main__':
    main()
