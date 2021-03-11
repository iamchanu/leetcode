from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_partial(start: int, end: int, depth: int):
            indent = " "*depth
            # print(f"{indent}search_partial({start}, {end})")
            if start == end:
                result = -1
            elif start+1 == end:
                if nums[start] == target:
                    result = start
                else:
                    result = -1
            else:
                first = nums[start]
                last = nums[end-1]
                if first < last and (target < first or last < target):
                    result = -1
                else:
                    mid = (start + end) // 2
                    result1 = search_partial(start, mid, depth=depth+1) 
                    if result1 != -1:
                        result = result1
                    else:
                        result = search_partial(mid, end, depth=depth+1)
            # print(f"{indent} >> {result}")
            return result

        return search_partial(0, len(nums), depth=0) 


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(4, self.solution.search([4,5,6,7,0,1,2], 0))
        self.assertEqual(-1, self.solution.search([4,5,6,7,0,1,2], 3))
        self.assertEqual(-1, self.solution.search([1], 0))


if __name__ == '__main__':
    unittest.main()
