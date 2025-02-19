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

    def _array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        node = head
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head

    def _list_to_array(self, head):
        if not head:
            return []
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def test_AddTwoNumbersTest_Empty(self):
        solution = _0002_AddTwoNumbers()
        head = s.addTwoNumbers(None, None)
        self.assertIsNone(head)

#   def test_add_two_numbers(self):
#       s = _0002_AddTwoNumbers()
#       for i, o in [(([], []), []),
#                 (([0], [1]), [1]),
#                 (([1, 8], [0]), [1, 8]),
#                 (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
#                 (([0, 1], [9, 9, 9, 9]), [9, 0, 0, 0, 1])]:
#         head = s.addTwoNumbers(self._array_to_list(
#             i[0]), self._array_to_list(i[1]))
#         arr = self._list_to_array(head)
#         self.assertEqual(arr, o)

if __name__ == '__main__':
    unittest.main()