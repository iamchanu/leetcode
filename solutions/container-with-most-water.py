from typing import List
import unittest

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sorted_indexes = sorted(
            list(range(len(heights))),
            key=lambda i: heights[i],
            reverse=True
        )

        leftmost = min(sorted_indexes[0], sorted_indexes[1])
        rightmost = max(sorted_indexes[0], sorted_indexes[1])
        max_area = min(heights[leftmost], heights[rightmost]) * (rightmost - leftmost)

        # print(f"leftmost={leftmost}, rightmost={rightmost}, max_area={max_area}")

        for i in sorted_indexes[2:]:
            area_to_left = heights[i] * abs(i - leftmost)
            area_to_right = heights[i] * abs(rightmost - i)
            # print(f"i={i}, heights[i]={heights[i]}, area_to_left={area_to_left}, area_to_right={area_to_right}")
            max_area = max(max_area, area_to_left, area_to_right)
            leftmost = min(leftmost, i)
            rightmost = max(i, rightmost)
            # print(f"leftmost={leftmost}, rightmost={rightmost}, max_area={max_area}")

        return max_area


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(49, self.solution.maxArea([1,8,6,2,5,4,8,3,7]))


if __name__ == '__main__':
    unittest.main()
