from typing import List
import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        PARENTHESES = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        OPENINGS = PARENTHESES.values()
        CLOSINGS = PARENTHESES.keys()

        stack = []
        for ch in s:
            if ch in OPENINGS:
                stack.append(ch)
            elif ch in CLOSINGS:
                if stack and PARENTHESES[ch] == stack.pop():
                    pass
                else:
                    return False

        return not stack            
        

class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(True, self.solution.isValid("()"))
        self.assertEqual(True, self.solution.isValid("()[]{}"))
        self.assertEqual(False, self.solution.isValid("(]"))
        self.assertEqual(False, self.solution.isValid("([)]"))
        self.assertEqual(True, self.solution.isValid("{[]}"))
        self.assertEqual(False, self.solution.isValid("}"))


if __name__ == '__main__':
    unittest.main()
