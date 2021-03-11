from typing import List
import unittest

def IDsOfmovies(flightDuration, numMovies, movieDuration):
    duration_sum = flightDuration - 30
    duration_dict = dict()

    picked = None
    picked_max_duration = 0
    for i in range(numMovies):
        duration = movieDuration[i]
        duration_dict[duration] = i

        target_duartion = duration_sum - duration
        if target_duartion in duration_dict:
            pair = (duration_dict[target_duartion], i)
            max_duration = max(duration, target_duartion)
            if max_duration > picked_max_duration:
                picked = pair
                picked_max_duration = max_duration

    if picked is not None:
        return picked
    else:
        return (-1, -1)


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual((2, 3), IDsOfmovies(90, 5, [1, 10, 25, 35, 60]))
        self.assertEqual((-1, -1), IDsOfmovies(90, 5, [10, 10, 10, 10, 10]))
        self.assertEqual((1, 2), IDsOfmovies(250, 5, [100, 180, 40, 120, 10]))


if __name__ == '__main__':
    unittest.main()
