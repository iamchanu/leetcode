from typing import List
import unittest

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        
        distances = {}
        
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0:
                    if j == 0:
                        distances[(i, j)] = 0
                    else:
                        distances[(i, j)] = j
                else:
                    if j == 0:
                        distances[(i, j)] = i
                    else:
                        c1 = word1[i-1]
                        c2 = word2[j-1]

                        up = distances[(i-1, j)] + 1
                        left = distances[(i, j-1)] + 1
                        up_left = distances[(i-1, j-1)] + (0 if c1 == c2 else 1)

                        distances[(i, j)] = min(up, left, up_left)

                        # print(f"substr1={word1[:i]}, substr2={word2[:j]}, distance={distances[(i,j)]} (up={up}, left={left}, up_left={up_left})")

        return distances[(len1, len2)]


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        # self.assertEqual(3, self.solution.minDistance("horse", "ros"))
        # self.assertEqual(5, self.solution.minDistance("intention", "execution"))
        self.assertEqual(10, self.solution.minDistance("zoologicoarchaeologist", "zoogeologist"))


if __name__ == '__main__':
    unittest.main()
