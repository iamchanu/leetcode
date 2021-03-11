from typing import List
import unittest

class Solution:
    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)

        idx = 0
        next_positive = 1
        while idx < len(nums):
            # print(f"idx={idx}, nums[idx]={nums[idx]}")
            if nums[idx] <= 0:
                # print("skipping non-positive")
                pass
            else:
                if nums[idx] in (next_positive, next_positive-1):
                    # print(f"nums[idx] == next_positive(={next_positive})")
                    next_positive = nums[idx] + 1
                else:
                    # print(f"nums[idx] 1= next_positive(={next_positive})")
                    break
            idx += 1
    
        return next_positive    


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(3, self.solution.firstMissingPositive([1,2,0]))
        self.assertEqual(2, self.solution.firstMissingPositive([3,4,-1,1]))
        self.assertEqual(1, self.solution.firstMissingPositive([7,8,9,11,12]))
        self.assertEqual(1, self.solution.firstMissingPositive([0,-1,-2]))
        self.assertEqual(3, self.solution.firstMissingPositive([0,2,2,1,1]))


if __name__ == '__main__':
    unittest.main()
