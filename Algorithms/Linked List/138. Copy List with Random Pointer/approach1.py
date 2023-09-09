from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        hashmap = {}
        copied_head = head
        while copied_head:
            hashmap[copied_head] = Node(copied_head.val)
            copied_head = copied_head.next
        copied_head = head
        while copied_head:
            if copied_head.next:
                hashmap[copied_head].next = hashmap[copied_head.next]
            if copied_head.random:
                hashmap[copied_head].random = hashmap[copied_head.random]
            copied_head = copied_head.next
        return hashmap[head]
