import sys
from typing import Optional

sys.path.append('../')
from Classes.ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class _0002_AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        current = result
        reminder = 0
        
        while (l1 is not None or l2 is not None):
            if result is None:
                result = ListNode()
                current = result
            
            if (l1 is not None):
                current.val += l1.val
                l1 = l1.next
                
            if (l2 is not None):
                current.val += l2.val
                l2 = l2.next
                
            if (current.val >= 10):
                reminder = 1
                current.val -= 10
                
            if (l1 is not None or l2 is not None or reminder > 0):
                current.next = ListNode(reminder)
                current = current.next
            
            reminder = 0
            
        return result
        