from typing import List
import unittest

class Solution:
    def make_anagram_key(self, s: str) -> str:
        char_dict = {}
        for ch in s:
            if ch not in char_dict:
                char_dict[ch] = 0
            char_dict[ch] += 1
        
        return ",".join([f"{ch}:{cnt}" for ch, cnt in sorted(list(char_dict.items()))])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            key = self.make_anagram_key(s)
            if key not in anagram_dict:
                anagram_dict[key] = list()
            anagram_dict[key].append(s)

        return list(anagram_dict.values())
        


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual(
            sorted([sorted(group) for group in [["bat"],["nat","tan"],["ate","eat","tea"]]]), 
            sorted([sorted(group) for group in self.solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])])
        )


if __name__ == '__main__':
    unittest.main()
