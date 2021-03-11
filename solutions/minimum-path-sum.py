from typing import List
import unittest
import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        min_path_sums = [None] * m
        for i in range(m):
            min_path_sums[i] = [None] * n
        
        min_path_sums[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                candidates = []
                if i != 0:
                    candidates.append(min_path_sums[i-1][j])

                if j != 0:
                    candidates.append(min_path_sums[i][j-1])

                min_path_sums[i][j] = min(candidates or [0]) + grid[i][j]

        # print(min_path_sums)
        return min_path_sums[m-1][n-1]


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(7, self.solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
        self.assertEqual(12, self.solution.minPathSum([[1,2,3],[4,5,6]]))


if __name__ == '__main__':
    unittest.main()
