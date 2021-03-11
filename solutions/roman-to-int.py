from typing import List
import unittest

class Solution:
    values_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        prev = None
        sum = 0
        for i in range(len(s)):
            val = self.values_dict[s[i]]

            sum += val
            if i > 0:
                if (s[i] in ("V", "X") and s[i-1] == "I") or \
                    (s[i] in ("L", "C") and s[i-1] == "X") or \
                    (s[i] in ("D", "M") and s[i-1] == "C"):
                    prev_val = self.values_dict[s[i-1]]
                    sum -= (2 * prev_val)

        return sum


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(3, self.solution.romanToInt("III"))
        self.assertEqual(4, self.solution.romanToInt("IV"))
        self.assertEqual(9, self.solution.romanToInt("IX"))
        self.assertEqual(58, self.solution.romanToInt("LVIII"))
        self.assertEqual(1994, self.solution.romanToInt("MCMXCIV"))


if __name__ == '__main__':
    unittest.main()
