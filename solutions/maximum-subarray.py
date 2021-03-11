from typing import List
import unittest

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_until_now = 0
        max_subarray = None
        min_containing_first = 0

        for num in nums:
            sum_until_now += num
            max_containing_now = sum_until_now - min_containing_first
            if max_subarray is not None:
                max_subarray = max(max_subarray, max_containing_now)
            else:
                max_subarray = max_containing_now
            min_containing_first = min(min_containing_first, sum_until_now)

        return max_subarray


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(6, self.solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        self.assertEqual(1, self.solution.maxSubArray([1]))
        self.assertEqual(0, self.solution.maxSubArray([0]))
        self.assertEqual(-1, self.solution.maxSubArray([-1]))
        self.assertEqual(-2147483647, self.solution.maxSubArray([-2147483647]))


if __name__ == '__main__':
    unittest.main()
