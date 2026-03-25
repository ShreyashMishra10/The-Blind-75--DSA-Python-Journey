class MyQueue:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(0)
        raise IndexError ('Deleting from empty stack')

    def peek(self) -> int:
        if not self.empty():
            return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()