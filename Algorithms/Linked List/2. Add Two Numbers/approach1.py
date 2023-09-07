from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numbers_to_linkedlist(number):
    if not number:
        return ListNode(0)
    head = None
    while number:
        digit = number % 10
        new_node = ListNode(digit)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
        number //= 10
    return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 1
        result = 0
        while l1 or l2:
            _sum = 0
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            result += (x * ( _sum ))
            x *= 10
        return numbers_to_linkedlist(result)