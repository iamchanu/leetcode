from typing import List
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, False)]
        sum = 0
        while queue:
            node, is_left = queue.pop(0)
            is_leaf = True

            if node.left:
                is_leaf = False
                queue.append((node.left, True))
            if node.right:
                is_leaf = False
                queue.append((node.right, False))

            if is_leaf and is_left:
                sum += node.val

        return sum


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(24, self.solution.sumOfLeftLeaves(
            TreeNode(3, 
                TreeNode(9, None, None), 
                TreeNode(20, 
                    TreeNode(15, None, None),
                    TreeNode(7, None, None),
                ),
            )
        ))


if __name__ == '__main__':
    unittest.main()
