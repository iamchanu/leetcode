from typing import List
import unittest

class Solution:
    def foo(self):
        pass
        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(False, self.solution.foo())


if __name__ == '__main__':
    unittest.main()
