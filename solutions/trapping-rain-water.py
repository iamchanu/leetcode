from typing import List
import unittest

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_walls = [0] * n
        water_levels = [0] * n

        maximum = 0
        for i in range(n):
            maximum = max(maximum, height[i])
            left_walls[i] = maximum

        maximum = 0
        for i in reversed(range(n)):
            maximum = max(maximum, height[i])
            water_levels[i] = min(left_walls[i], maximum)

        total_volume = sum(water_levels)
        wall_volume = sum(height)
        water_volume = total_volume - wall_volume
        return water_volume


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(6, self.solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        self.assertEqual(9, self.solution.trap([4,2,0,3,2,5]))


     #
#    #    # 
#  # ##  ##  #
## ##### ### #
## ###########


if __name__ == '__main__':
    unittest.main()
