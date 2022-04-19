class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._top = 0
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)
        self._top += 1

    def pop(self) -> None:
        if self._top > 0:
            self.items.pop()
            self._top -= 1

    def top(self) -> int:
        return self.items[self._top - 1]

    def getMin(self) -> int:
        _min = (2 ** 63) - 1
        for i in self.items:
            if i < _min:
                _min = i

        return _min


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
