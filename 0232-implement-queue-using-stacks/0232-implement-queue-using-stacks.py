from queue import LifoQueue

class MyQueue:

    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()

    def push(self, x: int) -> None:
        while not self.input.empty():
            self.output.put(self.input.get())
        self.input.put(x)
        while not self.output.empty():
            self.input.put(self.output.get())

    def pop(self) -> int:
        if self.input.qsize() == 0:
            return 0
        return self.input.get()

    def peek(self) -> int:
        if self.input.qsize() == 0:
           return 0
        return self.input.queue[-1]


    def empty(self) -> bool:
        return self.input.qsize() == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()