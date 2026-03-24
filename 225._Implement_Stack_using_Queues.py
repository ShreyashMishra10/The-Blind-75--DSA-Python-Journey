class MyStack:
    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]
        else:
            return None

    def empty(self) -> bool:
        return not self.stack