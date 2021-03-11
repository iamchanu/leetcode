from typing import List
import unittest

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        while nums:
            num = nums.pop(0)
            counts[num] += 1
        
        for num in range(3):
            cnt = counts[num]
            for _ in range(cnt):
                nums.append(num)
        return None


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        nums1 = [2,0,2,1,1,0]
        self.solution.sortColors(nums1)
        self.assertEqual([0,0,1,1,2,2], nums1)

        nums2 = [2,0,1]
        self.solution.sortColors(nums2)
        self.assertEqual([0,1,2], nums2)

        nums3 = [0]
        self.solution.sortColors(nums3)
        self.assertEqual([0], nums3)

        nums4 = [1]
        self.solution.sortColors(nums4)
        self.assertEqual([1], nums4)


if __name__ == '__main__':
    unittest.main()
