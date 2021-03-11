from typing import List
import unittest

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges_from = [set() for _ in range(numCourses)]
        edges_to = [set() for _ in range(numCourses)]
        for edge in prerequisites:
            dst, src = edge[0], edge[1]
            edges_from[src].add(dst)
            edges_to[dst].add(src)

        order = []
        queue = []

        for i in range(numCourses):
            if not edges_to[i]:
                queue.append(i)

        while queue:
            # print()
            # print(f"queue={queue}")
            src = queue.pop(0)
            order.append(src)

            for dst in edges_from[src]:
                edges_to[dst].remove(src)
                if not edges_to[dst]:
                    queue.append(dst)

        return order


class SolutionTest(unittest.TestCase):
    solution = Solution()
    def test_solution(self):
        self.assertIn(self.solution.findOrder(2, [[1,0]]), [[0,1]])
        self.assertIn(self.solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]), [[0,1,2,3], [0,2,1,3]])
        self.assertIn(self.solution.findOrder(2, [[0,1]]), [[1,0]])
        self.assertIn(self.solution.findOrder(3, [[2,0],[2,1]]), [[1,0,2],[0,1,2]])


if __name__ == '__main__':
    unittest.main()
