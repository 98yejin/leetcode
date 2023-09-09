from typing import Optional

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copied_head = head
        while copied_head:
            new_node = Node(copied_head.val)
            new_node.next = copied_head.next
            copied_head.next = new_node
            copied_head = new_node.next

        copied_head = head
        while copied_head:
            if copied_head.random:
                copied_head.next.random = copied_head.random.next
            copied_head = copied_head.next.next

        copied_head = head
        new_head = head.next
        new_copied_head = new_head
        while copied_head:
            copied_head.next = new_copied_head.next
            copied_head = copied_head.next
            if copied_head:
                new_copied_head.next = copied_head.next
                new_copied_head = new_copied_head.next

        return new_head
