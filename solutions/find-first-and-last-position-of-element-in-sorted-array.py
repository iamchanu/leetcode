from typing import List
import unittest

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRangeInner(nums, 0, len(nums), target) or [-1, -1]
        
    def searchRangeInner(self, nums, start, end, target):
        print(f"start={start}, end={end}, part={nums[start:end]}")
        if start == end:
            return None
        elif start + 1 == end:
            value = nums[start]
            if value == target:
                return [start, start]
            else:
                return None
        
        mid = (start + end) // 2
        if mid == 0 or nums[mid-1] < target:
            left = None
            right = self.searchRangeInner(nums, mid, end, target)
        elif nums[mid] > target:
            left = self.searchRangeInner(nums, start, mid, target)
            right = None
        else:
            left = self.searchRangeInner(nums, start, mid, target)
            right = self.searchRangeInner(nums, mid, end, target)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return [left[0], right[1]]


        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        # self.assertEqual([3, 4], self.solution.searchRange([5,7,7,8,8,10], 8))
        self.assertEqual([-1, -1], self.solution.searchRange([5,7,7,8,8,10], 6))
        # self.assertEqual([-1, -1], self.solution.searchRange([], 0))


if __name__ == '__main__':
    unittest.main()
