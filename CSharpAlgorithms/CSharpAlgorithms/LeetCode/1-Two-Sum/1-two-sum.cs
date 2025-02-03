public class Solution
{
  public int[] TwoSum(int[] nums, int target)
  {
    for (int i = 0; i < nums.Count(); i++)
    {
      for (int j = i + 1; j < nums.Count(); j++)
      {
        if (target == nums[i] + nums[j])
          return [i, j];
      }
    }
    return [];
  }
}