# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def list_to_linked_list(data):
    head = ListNode(data[0])
    current = head
    for i in range(1, len(data)):
        current.next = ListNode(data[i])
        current = current.next

    return head


def print_list(data):
    current = data
    while current:
        print(current.val, end=' ')
        current = current.next
    print()


def main():
    data = [1, 2, 3, 4, 5, 6]
    my_list = list_to_linked_list(data)
    print_list(my_list)
    middle = Solution().middleNode(my_list)
    print_list(middle)


if __name__ == "__main__":
    main()
