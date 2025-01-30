using System;

namespace LeetCode
{
  public class Solution
  {
    public class ListNode
    {
      public int val;
      public ListNode next;
      public ListNode(int val = 0, ListNode next = null)
      {
        this.val = val;
        this.next = next;
      }
    }

    public static ListNode arrayToListNode(int[] array)
    {
      ListNode node = new ListNode(array[0]);

      var current = node;
      for (int i = 1; i < array.Length; i++)
      {
        current.next = new ListNode(array[i]);
        current = current.next;
      }

      return node;
    }

    public static ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
      ListNode result = new ListNode(0);
      bool remainder = false;
      bool condition = l1.next != null && l2.next != null || l1.next != null ^ l2.next != null;
      var current = result;

      do
      {
        var val1 = l1 != null ? l1.val : 0;
        var val2 = l2 != null ? l2.val : 0;

        current.val = current.val + val1 + val2;

        if (current.val > 9)
        {
          remainder = true;
          current.val = current.val - 10;
        }
        else
        {
          remainder = false;
        }

        condition = l1.next != null && l2.next != null || l1.next != null ^ l2.next != null;
        if ()
        {
          l1 = l1.next;
          l2 = l2.next;

          if (remainder)
          {
            current.next = new ListNode(1);
            remainder = false;
          }
          else
          {
            current.next = new ListNode(0);
          }
          current = current.next;
        }
        while (condition);

      }

      return result;
    }
  }

  public class Program
  {
    static void Main(string[] args)
    {
      Solution.ListNode l1 = Solution.arrayToListNode(new int[] { 2, 4, 3 });
      Solution.ListNode l2 = Solution.arrayToListNode(new int[] { 5, 6, 4 });

      var result = Solution.AddTwoNumbers(l1, l2);
      var current = result;

      for (int i = 0; i < 3; i++)
      {
        Console.WriteLine(current.val);
        current = current.next;
      }
    }
  }
}