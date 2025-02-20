import sys
sys.path.append('../')

import unittest
from Classes.ListNode import ListNode
from Solutions._0002_AddTwoNumbers import _0002_AddTwoNumbers

class _0002_AddTwoNumbers_Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _arrayToListNode(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        node = head
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head

    def _listNodeToArray(self, head):
        if not head:
            return []
        arr = []
        node = head
        while node is not None and node.val is not None:
            arr.append(node.val)
            node = node.next
        return arr

    def test_AddTwoNumbersTest_Empty(self):
        listNode = self._arrayToListNode([])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode, listNode)
        self.assertEqual(self._listNodeToArray(result), [])

    def test_AddTwoNumbersTest_General(self):
        listNode = self._arrayToListNode([2, 4, 3])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode, listNode)
        self.assertEqual(self._listNodeToArray(result), [4, 8, 6])
        
    def test_AddTwoNumbersTest_General2(self):
        listNode1 = self._arrayToListNode([2, 4, 3])
        listNode2 = self._arrayToListNode([5, 6, 4])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [7, 0, 8])
        
    def test_AddTwoNumbersTest_HasCarry(self):
        listNode1 = self._arrayToListNode([9, 9, 9])
        listNode2 = self._arrayToListNode([9, 9, 9])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [8, 9, 9, 1])
        
    def test_AddTwoNumbersTest_HasCarry2(self):
        listNode1 = self._arrayToListNode([2, 4, 3])
        listNode2 = self._arrayToListNode([5, 6, 4])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [7, 0, 8 ]) 
    
    def test_AddTwoNumbersTest_HasMultipleCarry(self):
        listNode1 = self._arrayToListNode([ 1 ])
        listNode2 = self._arrayToListNode([ 9, 9])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [0, 0, 1])
        
    def test_AddTwoNumbersTest_FirstNumCarry(self):
        listNode1 = self._arrayToListNode([ 3, 4, 4 ])
        listNode2 = self._arrayToListNode([ 3, 4, 6 ])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [6, 8, 0, 1])
        
    def test_AddTwoNumbersTest_L1Longer(self):
        listNode1 = self._arrayToListNode([ 2, 4, 3, 1 ])
        listNode2 = self._arrayToListNode([ 5, 6, 4 ])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [ 7, 0, 8, 1 ])
        
    def test_AddTwoNumbersTest_L1Longer_2(self):
        listNode1 = self._arrayToListNode([ 1, 8 ])
        listNode2 = self._arrayToListNode([ 0 ])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [ 1, 8 ])
        
    def test_AddTwoNumbersTest_L1Empty(self):
        listNode1 = self._arrayToListNode(None)
        listNode2 = self._arrayToListNode([ 1, 8 ])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [ 1, 8 ])
    
    def test_AddTwoNumbersTest_L2Longer(self):
        listNode1 = self._arrayToListNode([ 2, 4, 3 ])
        listNode2 = self._arrayToListNode([ 5, 6, 4, 3 ])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [ 7, 0, 8, 3 ])
    
    def test_AddTwoNumbersTest_L2Longer_2(self):
        listNode1 = self._arrayToListNode([ 0 ])
        listNode2 = self._arrayToListNode([ 1, 8 ])
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [ 1, 8 ])

    def test_AddTwoNumbersTest_L2Empty(self):
        listNode1 = self._arrayToListNode([ 1, 8 ])
        listNode2 = self._arrayToListNode(None)
        solution = _0002_AddTwoNumbers()
        result = solution.addTwoNumbers(listNode1, listNode2)
        self.assertEqual(self._listNodeToArray(result), [ 1, 8 ])

if __name__ == '__main__':
    unittest.main()