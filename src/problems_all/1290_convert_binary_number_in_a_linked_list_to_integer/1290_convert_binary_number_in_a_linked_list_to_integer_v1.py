"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


Runtime: 33 ms
Memory: 13.9 MB
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/870483583/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        values = []
        current = head

        while current is not None:
            values.append(str(current.val))
            current = current.next

        binary = ''.join(values)
        decimal = int(binary, 2)

        return decimal


def main():
    head = ListNode(1, next=ListNode(0, next=ListNode(1)))
    result = Solution().getDecimalValue(head)
    print(result)


if __name__ == '__main__':
    main()
