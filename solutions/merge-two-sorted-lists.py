from typing import List
import unittest
from utils.linkedlist import ListNode, to_linked_list, from_linked_list, print_node

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0, None)
        current = dummy

        while l1 and l2:
            v1, v2 = l1.val, l2.val
            if v1 < v2:
                current.next = ListNode(v1, None)
                l1 = l1.next
            else:
                current.next = ListNode(v2, None)
                l2 = l2.next
            current = current.next
        
        while l1:
            current.next = ListNode(l1.val, None)
            l1 = l1.next
            current = current.next

        while l2:
            current.next = ListNode(l2.val, None)
            l2 = l2.next
            current = current.next

        return dummy.next
        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(
            [1,1,2,3,4,4], 
            from_linked_list(self.solution.mergeTwoLists(
                to_linked_list([1,2,4]),
                to_linked_list([1,3,4]),
            )))
        self.assertEqual(
            [], 
            from_linked_list(self.solution.mergeTwoLists(
                to_linked_list([]),
                to_linked_list([]),
            )))
        self.assertEqual(
            [0], 
            from_linked_list(self.solution.mergeTwoLists(
                to_linked_list([]),
                to_linked_list([0]),
            )))


if __name__ == '__main__':
    unittest.main()
