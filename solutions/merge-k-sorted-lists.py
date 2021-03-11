from typing import List
from utils.linkedlist import *
from heapq import *
import unittest

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        dummy_head = ListNode(val=None)
        current = dummy_head

        for idx, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, idx))

        while heap:
            val, idx = heappop(heap)
            
            node = lists[idx]
            next_node = node.next
            lists[idx] = next_node
            if next_node:
                heappush(heap, (next_node.val, idx))

            new_node = ListNode(val=val)
            current.next = new_node
            current = new_node
        
        return dummy_head.next

        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(
            [1,1,2,3,4,4,5,6], 
            from_linked_list(
                self.solution.mergeKLists(
                    list(map(to_linked_list, [[1,4,5],[1,3,4],[2,6]]))
                )
            ),
        )
        self.assertEqual(
            [], 
            from_linked_list(
                self.solution.mergeKLists(
                    map(to_linked_list, [])
                )
            ),
        )
        self.assertEqual(
            [], 
            from_linked_list(
                self.solution.mergeKLists(
                    map(to_linked_list, [[]])
                )
            ),
        )


if __name__ == '__main__':
    unittest.main()
