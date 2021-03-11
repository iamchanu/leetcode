from typing import List, Set, Dict
import unittest
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        result = set()
        for i in range(n-2):
            target = -nums[i]
            j, k = i+1, n-1
            while j != k:
                s = nums[j] + nums[k]
                if s == target:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

                if s >= target:
                    k = k-1
                else:
                    j = j+1

        return [list(t) for t in result]


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def sortListList(self, listlist):
        return sorted(map(lambda l: sorted(l), listlist))

    def test_solution(self):
        # self.assertEqual(
        #     self.sortListList([[-1, 0, 1], [-1, -1, 2]]),
        #     self.sortListList(self.solution.threeSum([-1, 0, 1, 2, -1, -4]))
        # )
        self.assertEqual(
            self.sortListList([[0, 0, 0]]),
            self.sortListList(self.solution.threeSum([0] * 3000))
        )


if __name__ == '__main__':
    unittest.main()
