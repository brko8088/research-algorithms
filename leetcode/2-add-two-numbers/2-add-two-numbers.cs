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
      var current = result;

      while (l1 != null || l2 != null)
      {
        Console.WriteLine("+ l1.val {0} && l2.val {1}", l1.val, l2.val);
        current.val = current.val + l1.val + l2.val;

        if (current.val > 9)
        {
          current.val = current.val - 10;
          current.next = new ListNode(1);
        }

        if (l1.next != null || l2.next != null)
        {
          l1 = (l1.next != null) ? l1.next : null;
          l2 = (l2.next != null) ? l2.next : null;

          if (current.next == null)
          {
            current.next = new ListNode(0);
          }
          current = current.next;
        }
        else
        {
          break;
        }
        Console.ReadKey();
      }

      return result;
    }
  }

  public class Program
  {
    static void Main(string[] args)
    {
      // Test 1
      Solution.ListNode l1 = Solution.arrayToListNode(new int[] { 2, 4, 3 });
      Solution.ListNode l2 = Solution.arrayToListNode(new int[] { 5, 6, 4 });

      Console.WriteLine("Start 1");
      var result1 = Solution.AddTwoNumbers(l1, l2);
      var current1 = result1;

      Console.WriteLine("Output 1");
      while (current1 != null)
      {
        Console.WriteLine(current1.val);
        current1 = (current1.next != null) ? current1.next : null;
      }
      Console.WriteLine("End 1");

      // Test 2
      Solution.ListNode l3 = Solution.arrayToListNode(new int[] { 9, 9, 9, 9, 9, 9, 9 });
      Solution.ListNode l4 = Solution.arrayToListNode(new int[] { 9, 9, 9, 9 });

      Console.WriteLine("Start 2");
      var result2 = Solution.AddTwoNumbers(l3, l4);
      var current2 = result2;

      Console.WriteLine("Output 2");
      while (current2 != null)
      {
        Console.WriteLine(current2.val);
        current2 = (current2.next != null) ? current2.next : null;
      }
      Console.WriteLine("End 2");

    }
  }
}