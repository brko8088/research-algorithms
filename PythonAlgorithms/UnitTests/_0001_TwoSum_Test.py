import sys
sys.path.append('../')

import unittest
from Solutions._0001_TwoSum import _0001_TwoSum

class _0001_TwoSum_Test(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_TwoSumTest_Ordered(self):
    nums = [2,7,11,15];
    target = 9;
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], 0)
    self.assertEqual(result[1], 1)
    
  def test_TwoSumTest_Unordered(self):
    nums = [ 5, 75, 25]
    target = 100;
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], 1)
    self.assertEqual(result[1], 2)
    
  def test_TwoSumTest_Duplicate(self):
    nums = [5, 5, 15, 30]
    target = 20
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], 1)
    self.assertEqual(result[1], 2)
    
  def test_TwoSumTest_Empty(self):
    nums = []
    target = 0
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 0)
    
  def test_TwoSumTest_Single(self):
    nums = [5]
    target = 5
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 0)
    
  def test_TwoSumTest_AllSame(self):
    nums = [5, 5, 5, 5, 5 ]
    target = 10
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], 0)
    self.assertEqual(result[1], 1)
    
  def test_TwoSumTest_NoTarget(self):
    nums = [2, 7, 11, 15]
    target = 5
    
    solution = _0001_TwoSum()
    result = solution.twoSum(nums, target)
    
    self.assertEqual(len(result), 0)
    
  # def TwoSumTest_LargeArray(self):
  #   nums = [i for i in range(0, 1000000)]
  #   target = 19082
    
  #   solution = _0001_TwoSum()
  #   result = solution.twoSum(nums, target)
    
  #   self.assertEqual(len(result), 2)
  #   self.assertEqual(result[0], 0)
  #   self.assertEqual(result[1], 999999)

if __name__ == '__main__':
    unittest.main()