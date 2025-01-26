class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    arrayLength = len(nums)
    rtype = []
    
    for i in range(0, arrayLength):
      for j in range (i + 1, arrayLength):
        if (nums[i] + nums[j] == target):
          rtype.append(i)
          rtype.append(j)
          return rtype