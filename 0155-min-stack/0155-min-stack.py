class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        mini = val
        if len(self.st):
            mini = min(self.st[-1][1],mini)
        self.st.append([val,mini])

    def pop(self) -> None:
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()