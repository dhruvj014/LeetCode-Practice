class MinStack:

    def __init__(self):
        self.st = []
        self.mini = 0

    def push(self, val: int) -> None:
        if not len(self.st):
            self.mini = val
            self.st.append(val)
        else:
            if(val > self.mini):
                self.st.append(val)
            else:
                self.st.append((2*val)-self.mini)
                self.mini = val
    def pop(self) -> None:
        if not len(self.st):
            return
        x = self.st[-1]
        self.st.pop()
        if(x<self.mini):
            self.mini = (2*self.mini) - x

    def top(self) -> int:
        if not len(self.st):
            return
        x = self.st[-1]
        if (self.mini<x):
            return x
        return self.mini
    def getMin(self) -> int:
        return self.mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()