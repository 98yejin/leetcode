from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # initialize two pointers, one slow (tortoise) and one fast (hare), both starting at the head of the linked list.
        slow = head 
        fast = head.next
        while slow != fast:
            # If there is no cycle in the linked list, the fast pointer will eventually reach the end of the list, and you can conclude that there is no cycle.
            if fast is None or fast.next is None:
                return False
            # Move the slow pointer one step at a time and the fast pointer two steps at a time.
            slow = slow.next
            fast = fast.next.next 
        # If there is a cycle, the fast pointer will eventually catch up to the slow pointer, and they will meet within the cycle.
        return True