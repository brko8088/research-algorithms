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

  public class Program
  {
    static void Main(string[] args)
    {
      // Test 0
      runProgram(new int[] { 0 }, new int[] { 0 }, 0);

      // Test 1
      runProgram(new int[] { 9 }, new int[] { 9 }, 1);

      // Test 2
      runProgram(new int[] { 2, 4, 3 }, new int[] { 5, 6, 4 }, 2);

      // Test 3
      runProgram(new int[] { 9, 9, 9, 9, 9, 9, 9 }, new int[] { 9, 9, 9, 9 }, 3);
    }

    static void runProgram(int[] a1, int[] a2, int i)
    {
      Solution.ListNode l1 = Solution.arrayToListNode(a1);
      Solution.ListNode l2 = Solution.arrayToListNode(a2);

      Console.WriteLine("Start {0}", i);
      var result = Solution.AddTwoNumbers(l1, l2);
      var current = result;

      Console.WriteLine("Output {0}", i);
      while (current != null)
      {
        Console.WriteLine(current.val);
        current = (current.next != null) ? current.next : null;
      }
      Console.WriteLine("End {0}", i);
    }
  }
}