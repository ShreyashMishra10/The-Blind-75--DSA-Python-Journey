class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def pushRight(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def popLeft(self):
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.cache = {}
        self.freq_map = {}

    def _update(self, node):
        f = node.freq
        self.freq_map[f].pop(node)
        if self.min_freq == f and self.freq_map[f].size == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update(node)
        else:
            if len(self.cache) == self.cap:
                evict_node = self.freq_map[self.min_freq].popLeft()
                del self.cache[evict_node.key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()
        self.freq_map[1].pushRight(new_node)
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)