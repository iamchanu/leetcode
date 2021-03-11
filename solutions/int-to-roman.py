from typing import List
import unittest

class Solution:
    def intToRoman(self, num: int) -> str:
        ONE, FIVE = 0, 1
        NUMERALS = [
            ('I', 'V'),
            ('X', 'L'),
            ('C', 'D'),
            ('M',),
        ]
        
        roman = ""
        for digit in reversed(range(len(NUMERALS))):
            power10 = 10 ** digit
            n = (num // power10) % 10
            
            s = ""
            if n == 0:
                pass
            elif 1 <= n < 4:
                s = NUMERALS[digit][ONE] * n
            elif n == 4:
                s = NUMERALS[digit][ONE] + NUMERALS[digit][FIVE]
            elif n == 5:
                s = NUMERALS[digit][FIVE]
            elif 6 <= n < 9:
                s = NUMERALS[digit][FIVE] + (NUMERALS[digit][ONE] * (n-5))
            else: # n == 9
                s = NUMERALS[digit][ONE] + NUMERALS[digit+1][ONE]
            
            roman += s
        
        return roman

class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual("III", self.solution.intToRoman(3))
        self.assertEqual("IV", self.solution.intToRoman(4))
        self.assertEqual("IX", self.solution.intToRoman(9))
        self.assertEqual("LVIII", self.solution.intToRoman(58))
        self.assertEqual("MCMXCIV", self.solution.intToRoman(1994))


if __name__ == '__main__':
    unittest.main()
