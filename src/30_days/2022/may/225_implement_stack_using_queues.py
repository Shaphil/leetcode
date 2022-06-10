from collections import deque


class MyStack:

    def __init__(self):
        self.queue_push = deque()
        self.queue_pop = deque()

    def move_to_pop(self):
        length = len(self.queue_push) - 1
        for _ in range(length):
            self.queue_pop.append(self.queue_push.popleft())

    def move_to_push(self):
        length = len(self.queue_pop)
        for _ in range(length):
            self.queue_push.appendleft(self.queue_pop.pop())

    def push(self, x: int) -> None:
        self.queue_push.append(x)

    def pop(self) -> int:
        self.move_to_pop()
        val = self.queue_push.popleft()
        self.move_to_push()

        return val

    def top(self) -> int:
        self.move_to_pop()
        val = self.queue_push[0]
        self.move_to_push()

        return val

    def empty(self) -> bool:
        return len(self.queue_push) == 0


def main():
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.queue_push)
    print(stack.top())
    print(stack.queue_push)
    print(stack.pop())


if __name__ == '__main__':
    main()
