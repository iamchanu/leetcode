from typing import List
import unittest
import bisect

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        for interval in intervals:
            print(f"merged_intervals: {merged_intervals}")
            print(f"interval: {interval}")
            start, end = interval[0], interval[1]

            start_pos = bisect.bisect_left(merged_intervals, start)
            end_pos = bisect.bisect_right(merged_intervals, end)
            print(f"start={start}, start_pos={start_pos}")
            print(f"end={end}, end_pos={end_pos}")

            merged_intervals.insert(start_pos, start)
            merged_intervals.insert(end_pos+1, end)

            if start_pos % 2:
                remove_start = start_pos
            else:
                remove_start = start_pos + 1

            if end_pos % 2:
                remove_end = end_pos + 2
            else:
                remove_end = end_pos + 1

            print(f"remove_start={remove_start}, remove_end={remove_end}")
            del merged_intervals[remove_start:remove_end]

            print()
        print(f"merged_intervals: {merged_intervals}")

        answer = []
        for i in range(len(merged_intervals) // 2):
            answer.append([merged_intervals[2*i], merged_intervals[2*i+1]])

        return answer


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(
            [[1,6],[8,10],[15,18]], 
            self.solution.merge([[1,3],[2,6],[8,10],[15,18]])
        )
        self.assertEqual(
            [[1,5]], 
            self.solution.merge([[1,4],[4,5]])
        )
        self.assertEqual(
            [[1,4]], 
            self.solution.merge([[1,4],[2,3]])
        )


if __name__ == '__main__':
    unittest.main()


# []
# (0, 0)
# [1, 3]
# [0:0]


# [1, 3]
# (1, 2)
# [1, 2, 3, 6]
# [1,     , 6]
# [1:3]

# (0, 0) -> (1, 1)
# (1, 2) -> (1, 3)
# (1, 1) -> (1, 3)
# (0, 2) -> (1, 3)
# (2, 3) -> (3, 5)

# [1, 6, 8, 10]
# [0, 1, 6, 7, 8, 10]