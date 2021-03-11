from typing import List
import unittest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        import heapq
        
        for elem in nums:
            if len(heap) < k or elem > heap[0]:
                heapq.heappush(heap, elem)
            
            if len(heap) > k:
                heapq.heappop(heap)

            # print(heap)
        return heap[0]
        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(5, self.solution.findKthLargest([3,2,1,5,6,4], 2))
        self.assertEqual(4, self.solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))


if __name__ == '__main__':
    unittest.main()
