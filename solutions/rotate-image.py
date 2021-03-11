from typing import List
import unittest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pass


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.solution.rotate(matrix)
        self.assertEqual([[7,4,1],[8,5,2],[9,6,3]], matrix)

    def test_solution2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        self.solution.rotate(matrix)
        self.assertEqual([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], matrix)

    def test_solution3(self):
        matrix = [[1]]
        self.solution.rotate(matrix)
        self.assertEqual([[1]], matrix)

    def test_solution4(self):
        matrix = [[1,2],[3,4]]
        self.solution.rotate(matrix)
        self.assertEqual([[3,1],[4,2]], matrix)


if __name__ == '__main__':
    unittest.main()

