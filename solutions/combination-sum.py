from typing import List
import unittest

class Solution:
    def combinationSumRecur(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        elif target == 0:
            return [[]]

        n = candidates[0]
        if target < n:
            return []
        else:
            return \
                [[n]+combination for combination in self.combinationSumRecur(candidates, target-n)] + \
                self.combinationSumRecur(candidates[1:], target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumRecur(sorted(candidates), target)


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual([[2,2,3],[7]], self.solution.combinationSum([2,3,6,7], 7))
        self.assertEqual([[2,2,2,2],[2,3,3],[3,5]], self.solution.combinationSum([2,3,5], 8))
        self.assertEqual([], self.solution.combinationSum([2], 1))
        self.assertEqual([[1]], self.solution.combinationSum([1], 1))


if __name__ == '__main__':
    unittest.main()
