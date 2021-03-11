from typing import List
import unittest

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l, m, n = len(word), len(board), len(board[0])

        stack = [(None, None)]
        adj_of_stack = {
            (None, None): [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]
        }

        def get_adjacents(i, j, next_letter):
            adj = []
            for (i_offset, j_offset) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii, jj = i+i_offset, j+j_offset
                if (0 <= ii < m) and (0 <= jj < n) and board[ii][jj] == next_letter:
                    adj.append((ii, jj))
            # print(f"get_adjacents({i},{j},'{next_letter}'') = {adj}")
            return adj
        
        while stack:
            # print(stack)
            # print(adj_of_stack)
            if len(stack)-1 == len(word):
                return True

            i, j = stack[-1]
            next_letter = word[len(stack)-1]
            # print(f"i={i}, j={j}, next_letter={next_letter}")

            if (i, j) not in adj_of_stack:
                adj_of_stack[(i, j)] = get_adjacents(i, j, next_letter)

            adjacents = adj_of_stack[(i, j)]
            if adjacents:
                ii, jj = adjacents.pop(0)
                if ((ii, jj)) not in adj_of_stack:
                    stack.append((ii, jj))
            else:
                stack.pop()
                del adj_of_stack[(i, j)]
            # print()

        return False


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(True, self.solution.exist(
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            word = "ABCCED",
        ))
        self.assertEqual(False, self.solution.exist(
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            word = "ABCB",
        ))
        self.assertEqual(False, self.solution.exist(
            board = [["a","b"],["c","d"]],
            word = "abcd",
        ))
        self.assertEqual(True, self.solution.exist(
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            word = "SEE",
        ))
        self.assertEqual(True, self.solution.exist(
            board = [["C","A","A"],["A","A","A"],["B","C","D"]],
            word = "AAB",
        ))


if __name__ == '__main__':
    unittest.main()
