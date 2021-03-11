from typing import List
import unittest

class Solution:
    def all_longest_palindroms(self, s: str) -> List[str]:
        length = len(s)
        is_pal = [None] * (length+1)
        for i in range(length+1):
            if i in (0, 1):
                is_pal[i] = [True] * (length-i+1)
            else:
                is_pal[i] = [False] * (length-i+1)

                for j in range(length-i+1):
                    start, end = j, j+i
                    is_pal[i][j] = (s[j] == s[j+i-1]) and is_pal[i-2][j+1]
        
        for i in range(length, -1, -1):
            if any(is_pal[i]):
                # print(is_pal[i])
                return [s[j:j+i] for j in range(length-i+1) if is_pal[i][j]]
        
    def longestPalindrome(self, s: str) -> str:
        return self.all_longest_palindroms(s)[0]

class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertIn(self.solution.longestPalindrome("babad"), ["bab", "aba"])
        self.assertIn(self.solution.longestPalindrome("cbbd"), ["bb"])
        self.assertIn(self.solution.longestPalindrome(""), [""])


if __name__ == '__main__':
    unittest.main()
