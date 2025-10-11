# doubly-linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.deleteNode(node)
        self.insertAfterHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
            self.insertAfterHead(node)
        else:
            if(self.capacity == len(self.map)):
                node = self.tail.prev
                self.map.pop(node.key)
                self.deleteNode(node)
            node = Node(key, value)
            self.map[key] = node
            self.insertAfterHead(node)

    def insertAfterHead(self, node):
        currafter = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = currafter
        currafter.prev = node

    def deleteNode(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)