class StockSpanner:
    def __init__(self):
       self.arr = []
       self.ind = -1
       
    def next(self, price: int) -> int:
        self.ind += 1
        while(self.arr and self.arr[-1][0] <= price):
            self.arr.pop()
        if not self.arr:
            ans = self.ind - (-1)
        else:
            ans = self.ind - self.arr[-1][1]
        self.arr.append([price,self.ind])
        return ans



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)