def middleNode(head):
    length = 0
    current = head
    while current:
        current = current.next
        length += 1

    length = length // 2
    current = head
    while length > 0:
        current = current.next
        length -= 1

    return current


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    l = middleNode(a)
    print(l.val)
