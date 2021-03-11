from typing import List
import unittest

def get_failure(group):
    failure = [0] * len(group)
    j = 0
    for i in range(1, len(group)):
        fruit = group[i]
        while j > 0 and not (group[i] == group[j] or group[i] == "anything" or group[j] == "anything"):
            j = failure[j-1]
        if group[i] == group[j] or group[i] == "anything" or group[j] == "anything":
            j += 1
            failure[i] = j
    return failure

def checkWinner(codeList, shoppingCart):
    failures = [get_failure(group) for group in codeList]
    # print(f"failures: {failures}")
    # failures = [[0, 1], [0, 1, 2]]

    group_idx = 0
    fruit_idx = 0
    group, failure = codeList[group_idx], failures[group_idx]

    for fruit in shoppingCart:
        # print()
        # print(f"fruit={fruit}")
        # print(f"group={group}, fruit_idx={fruit_idx}")
        while fruit_idx > 0 and not (fruit == group[fruit_idx] or group[fruit_idx] == "anything"):
            fruit_idx = failure[fruit_idx-1]
            # print(f"failure: fruit_idx <- {fruit_idx}")

        # print(f"group={group}, fruit_idx={fruit_idx}")
        if fruit == group[fruit_idx] or group[fruit_idx] == "anything":
            if fruit_idx >= len(group)-1:
                group_idx += 1
                fruit_idx = 0
                # print(f"match: group_idx <- {group_idx}")
                if group_idx >= len(codeList):
                    return 1
                else:
                    group, failure = codeList[group_idx], failures[group_idx]
            else:
                fruit_idx += 1
                # print(f"match: fruit_idx <- {fruit_idx}")
    return 0


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(1, checkWinner([["apple", "apple"], ["banana", "anything", "banana"]], ["orage", "apple", "apple", "banana", "orange", "banana"]))
        self.assertEqual(0, checkWinner([["apple", "apple"], ["banana", "anything", "banana"]], ["banana", "orange", "banana", "apple", "apple"]))
        self.assertEqual(0, checkWinner([["apple", "apple"], ["banana", "anything", "banana"]], ["apple", "banana", "apple", "banana", "orange", "banana"]))
        self.assertEqual(0, checkWinner([["apple", "apple"], ["banana", "anything", "banana"]], ["apple", "apple", "apple", "banana"]))
        self.assertEqual(1, checkWinner([["apple", "apple"], ["banana", "anything", "banana"]], ["apple", "apple", "banana", "banana", "orange", "banana"]))


if __name__ == '__main__':
    unittest.main()
