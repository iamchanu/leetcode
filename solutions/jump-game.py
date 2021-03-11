from typing import List
import unittest

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        current = 0
        max_reachable = None

        while max_reachable is None or current <= max_reachable:
            reachable_from_here = current + nums[current]
            if max_reachable is not None:
                max_reachable = max(max_reachable, reachable_from_here)
            else:
                max_reachable = reachable_from_here
                
            if max_reachable >= last:
                return True
            current += 1

        return False


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(True, self.solution.canJump([2,3,1,1,4]))
        self.assertEqual(False, self.solution.canJump([3,2,1,0,4]))


if __name__ == '__main__':
    unittest.main()
