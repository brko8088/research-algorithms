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
        cl1 = l1
        cl2 = l2
        xl1 = []
        xl2 = []
        
        while (cl1 is not None or cl2 is not None):
            if (cl1 is not None):
                xl1.append(cl1.val)
                if (cl1.next is None):
                    cl1.val = 0
                cl1 = cl1.next
                
            if (cl2 is not None):
                xl2.append(cl2.val)
                if (cl2.next is None):
                    cl2.val = 0
                cl2 = cl2.next

        highest_number = 0 
        if (len(xl1) > len(xl2)):
            highest_number = len(xl1)
        else:
            highest_number = len(xl2)

        res_node = None
        cur_node = None
        carry_over = 0
        
        for x in range(0, highest_number):
            if (res_node is None):
                res_node = ListNode()
                carry_over = self.remCal(xl1, xl2, x, carry_over)
                res_node.val = ((self.calculation(xl1, xl2, x)) % 10)
                if x < (highest_number - 1) or carry_over > 0:
                    res_node.next = ListNode()
                    cur_node = res_node.next
                    cur_node.val = carry_over
                    
            else:
                carry_over = self.remCal(xl1, xl2, x, carry_over)
                cur_node.val = (cur_node.val + self.calculation(xl1, xl2, x))  % 10
                if x < (highest_number - 1) or carry_over > 0:
                    cur_node.next = ListNode()
                    cur_node = cur_node.next
                    cur_node.val = carry_over
        
        return res_node
        
    def calculation(self, a1, a2, x):
        if x < len(a1) and x < len(a2):
            return a1[x] + a2[x]
        elif x < len(a1):
            return a1[x]
        elif x < len(a2):
            return a2[x]
        else:
            return -1
                                   
    def remCal(self, a1, a2, x, carry_over):
        if (self.calculation(a1, a2, x) + carry_over) > 9:
            return 1
        return 0
    