from typing import List
import unittest

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # print(f"permute: {nums}")
        if not nums:
            return [[]]
        else:
            result = []
            for i in range(len(nums)):
                for perm in self.permute(nums[0:i] + nums[i+1:]):
                    result.append([nums[i]] + perm)
            return result


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(
            sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]), 
            sorted(self.solution.permute([1,2,3]))
        )
        self.assertEqual(
            sorted([[0,1],[1,0]]), 
            sorted(self.solution.permute([0,1]))
        )
        self.assertEqual(
            sorted([[1]]), 
            sorted(self.solution.permute([1]))
        )


if __name__ == '__main__':
    unittest.main()
