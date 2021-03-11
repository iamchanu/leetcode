from typing import List
import unittest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        row_nums = [None] * len(s)
        rows = [""] * numRows
        
        direction = True
        for i in range(len(s)):
            if i == 0:
                row_nums[i] = 0
            elif direction:
                row_nums[i] = row_nums[i-1] + 1
            else:
                row_nums[i] = row_nums[i-1] - 1
            
            rows[row_nums[i]] += (s[i])

            if row_nums[i] == 0:
                direction = True
            if row_nums[i] == numRows-1:
                direction = False

        # print(rows)
        return "".join(rows)
        


class SolutionTest(unittest.TestCase):
    solution = Solution()
    def test_solution(self):
        self.assertEqual("PAHNAPLSIIGYIR", self.solution.convert("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", self.solution.convert("PAYPALISHIRING", 4))
        self.assertEqual("ABC", self.solution.convert("ABC", 1))


if __name__ == '__main__':
    unittest.main()
