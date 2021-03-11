from typing import List
import unittest

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unvisiteds = [set() for _ in range(numCourses)]
        for edge in prerequisites:
            src, dst = edge[0], edge[1]
            unvisiteds[src].add(dst)

        visited = [False] * numCourses
        num_visited = 0

        while num_visited < numCourses:
            root = list(filter(lambda i: not visited[i], range(numCourses)))[0]
            # print(f"root={root}")

            in_stack = [False] * numCourses

            stack = [root]
            in_stack[root] = True

            while stack:
                # print()
                # print(f"stack={stack}")
                # print(f"in_stack={in_stack}")
                peek = stack[-1]

                if not visited[peek]:
                    visited[peek] = True
                    num_visited += 1
                # print(f"visited={visited}, num_visited={num_visited}")

                # print(f"unvisiteds={unvisiteds[peek]}")
                if unvisiteds[peek]:
                    _next = unvisiteds[peek].pop()
                    if in_stack[_next]:
                        return False
                    stack.append(_next)
                    in_stack[_next] = True
                else:
                    stack.pop()
                    in_stack[peek] = False

        return True


class SolutionTest(unittest.TestCase):
    solution = Solution()
    def test_solution(self):
        self.assertEqual(False, self.solution.canFinish(2, [[1,0],[0,1]]))
        self.assertEqual(True, self.solution.canFinish(2, [[1,0]]))


if __name__ == '__main__':
    unittest.main()
