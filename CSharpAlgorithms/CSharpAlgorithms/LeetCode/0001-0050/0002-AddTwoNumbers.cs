// https://leetcode.com/problems/add-two-numbers/
      
    
namespace LeetCode
{
    using System.Collections.Generic;
    public class _0002_AddTwoNumbers
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            ListNode current, result = new ListNode();
            int carry = 0, sum = 0;
            current = result;

            while (l1 != null || l2 != null)
            {
                current.next = new ListNode();
                current = current.next;
                sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
                carry = (sum % 10) == sum ? 0 : 1;
                l1 = l1?.next;
                l2 = l2?.next;
                current.val = sum % 10;
            }
            if (carry == 1)
                current.next = new ListNode(1);

            return result.next;
        }
    }
}