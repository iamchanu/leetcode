import unittest

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._next = None
        self._iter = self._get_combinations(characters, combinationLength)

    def next(self) -> str:
        if self.hasNext():
            tmp = self._next
            self._next = None
            return tmp
        else:
            return None

    def hasNext(self) -> bool:
        if self._next is None:
            try:
                self._next = self._iter.__next__()
            except StopIteration:
                return False
        return True

    def _get_combinations(self, characters, length):
        for i in range(len(characters)):
            if length == 1:
                yield characters[i]
            else:
                for combination in self._get_combinations(characters[i+1:], length-1):
                    yield characters[i] + combination



class SolutionTest(unittest.TestCase):
    def get_combinations(self, characters: str, combinationLength: int):
        combinations = []
        iterator = CombinationIterator(characters, combinationLength)
        while iterator.hasNext():
            combinations.append(iterator.next())
        return combinations

    def test_solution(self):
        self.assertListEqual(["ab", "ac", "bc"], self.get_combinations("abc", 2))
        self.assertListEqual(["abc"], self.get_combinations("abc", 3))
        self.assertListEqual(["abc", "abd", "abe", "acd", "ace", "ade", "bcd", "bce", "bde", "cde"], self.get_combinations("abcde", 3))


if __name__ == '__main__':
    unittest.main()
