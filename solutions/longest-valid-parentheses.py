from typing import List
import unittest

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        length = len(s)
        max_substr = 0
        prev_substrs = {}

        for i in range(length):
            ch = s[i]
            
            if ch == '(':
                stack.append(i)
                
            else:
                if stack:
                    prev = stack.pop(-1)
                    curr_substr = i - prev + 1

                    prev_substr = prev_substrs.get(prev-1, 0)
                    curr_substr += prev_substr
                    prev_substrs[i] = curr_substr

                    max_substr = max(max_substr, curr_substr)
                        
        return max_substr

        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(2, self.solution.longestValidParentheses("(()"))
        self.assertEqual(4, self.solution.longestValidParentheses(")()())"))
        self.assertEqual(0, self.solution.longestValidParentheses(""))
        self.assertEqual(2, self.solution.longestValidParentheses("()(()"))
        self.assertEqual(6, self.solution.longestValidParentheses("()(())"))
        self.assertEqual(4, self.solution.longestValidParentheses("()((())"))
        self.assertEqual(4, self.solution.longestValidParentheses("(()()"))


if __name__ == '__main__':
    unittest.main()
