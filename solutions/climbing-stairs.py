from typing import List
import unittest
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        m = n + 1
        sqrt5 = math.sqrt(5)
        k1 = (1 + sqrt5) / 2
        k2 = (1 - sqrt5) / 2

        fib = round((math.pow(k1, m) - math.pow(k2, m)) / sqrt5)
        return fib



class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(2, self.solution.climbStairs(2))
        self.assertEqual(3, self.solution.climbStairs(3))
        self.assertEqual(5, self.solution.climbStairs(4))
        self.assertEqual(8, self.solution.climbStairs(5))
        self.assertEqual(13, self.solution.climbStairs(6))
        self.assertEqual(21, self.solution.climbStairs(7))
        self.assertEqual(34, self.solution.climbStairs(8))


if __name__ == '__main__':
    unittest.main()
