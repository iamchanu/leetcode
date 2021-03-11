from typing import List
import unittest
from utils.linkedlist import *

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # print(f"head: {from_linked_list(head)}, n: {n}")
        front = head
        for _ in range(n):
            front = front.next
        # print(f"front: {print_node(front)}")

        rear = head
        rear_prev = None
        while front:
            # print(f"front: {print_node(front)}, rear: {print_node(rear)}")
            front = front.next
            rear_prev = rear
            rear = rear.next

        # print(f"rear: {print_node(rear)}, rear_prev: {print_node(rear_prev)}")
        if rear_prev:
            rear_prev.next = rear.next
        else:
            head = head.next
        # print()
        
        return head


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual([1,2,3,5], from_linked_list(
            self.solution.removeNthFromEnd(to_linked_list([1,2,3,4,5]), 2)
        ))
        self.assertEqual([], from_linked_list(
            self.solution.removeNthFromEnd(to_linked_list([1]), 1)
        ))
        self.assertEqual([1], from_linked_list(
            self.solution.removeNthFromEnd(to_linked_list([1,2]), 1)
        ))


if __name__ == '__main__':
    unittest.main()
