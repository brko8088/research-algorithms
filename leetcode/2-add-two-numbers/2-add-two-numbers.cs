/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution
{
  public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
  {
    ListNode result = new ListNode(0);
    bool remainder = false;

    if (l1.val !== null)
    {
      result.val += l1.val;
    }

    if (l2.val !== null)
    {
      result.val += l2.val;
    }

    if (result.val > 9)
    {
      result.next = new ListNode(1);
      result.
    }
    else
    {
      result.next = new ListNode(0);
    }
  }
}