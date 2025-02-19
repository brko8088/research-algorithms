from typing import List

class _0001_TwoSum(object):
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(0, len(nums)):
      for j in range (i + 1, len(nums)):
        if (nums[i] + nums[j] == target):
          return [i,j]
        
    return []