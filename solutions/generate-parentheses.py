from typing import List, Tuple
import unittest

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            one_pair_less = self.generateParenthesis(n-1)
            return \
                ["("+s+")" for s in one_pair_less] + \
                ["()"+s for s in one_pair_less] + \
                [s+"()" for s in one_pair_less if s[:2] != "()"]
        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(
            sorted(["(())","()()"]), 
            sorted(self.solution.generateParenthesis(2))
        )
        self.assertEqual(
            sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]), 
            sorted(self.solution.generateParenthesis(3))
        )
        self.assertEqual(
            sorted([
                "(((())))", "((()()))", "((())())", "(()(()))", "(()()())",
                "()((()))", "()(()())", "()(())()", "()()(())", "()()()()",
                "((()))()", "(()())()", "(())()()", "(())(())", 
            ]),
            sorted(self.solution.generateParenthesis(4))
        )

if __name__ == '__main__':
    unittest.main()
