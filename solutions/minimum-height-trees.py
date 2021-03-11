from typing import List
import unittest

class Solution:
    def visit(self, v):
        # print(f"visit {v}")
        self.visited[v] = True

        deepest = (None, 0)
        second_deepest = (None, 0)
        
        for w in self.edges[v]:
            if self.visited[w]: continue
            self.visit(w)
            
            depth_to_w = self.max_depth_child[w][1] + 1
            if depth_to_w >= deepest[1]:
                second_deepest = deepest
                deepest = (w, depth_to_w)
            elif depth_to_w >= second_deepest[1]:
                second_deepest = (w, depth_to_w)
              
        self.max_depth_child[v] = deepest
        self.max_pathlen_including[v] = deepest[1] + second_deepest[1]
        
                
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.visited = [False] * n
        self.edges = [[] for i in range(n)]
        self.max_depth_child = [None] * n # list of tuples: (child_with_max_depth, depth_toward_that_child)
        self.max_pathlen_including = [0] * n
        
        for edge in edges:
            v, w = edge[0], edge[1]
            self.edges[v].append(w)
            self.edges[w].append(v)
            
        self.visit(0)
        
        # print(self.max_depth_child)
        # print(self.max_pathlen_including)

        max_pathlen_overall = max(self.max_pathlen_including)
        mht_roots = set()

        import math
        for i in range(n):
            if self.max_pathlen_including[i] != max_pathlen_overall:
                continue
            v = i
            while self.max_depth_child[v][1] > math.ceil(max_pathlen_overall / 2):
                v = self.max_depth_child[v][0]

            mht_roots.add(v)
            if max_pathlen_overall % 2 != 0:
                mht_roots.add(self.max_depth_child[v][0])

        return list(mht_roots)


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual([1], self.solution.findMinHeightTrees(n = 4, edges = [[1, 0], [1, 2], [1, 3]]))
        self.assertEqual([3, 4], self.solution.findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
        self.assertEqual([3, 4], self.solution.findMinHeightTrees(n = 8, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [5, 6], [2, 7]]))


if __name__ == '__main__':
    unittest.main()
