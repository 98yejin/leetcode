class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.add(node)
            if len(self.hashmap) > self.capacity:
                del self.hashmap[self.tail.prev.key]
                self.remove(self.tail.prev)


            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)