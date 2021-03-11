from typing import List
import unittest

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, plen = 0, len(p)
        initial = State(i)

        prev_states = [initial]
        while i < plen:
            ch = p[i]
            new_state = State(i+1)
            # print(f"i={i}, prev_states={[p.idx for p in prev_states]}")
            for prev in prev_states:
                prev.add_transition(ch, new_state)

            if i+1 < plen and p[i+1] == "*":
                new_state.add_transition(ch, new_state)
                prev_states.append(new_state)
                i += 2
            else:
                prev_states = [new_state]
                i += 1
            
            if i >= plen:
                new_state.set_final()

        visited = set()
        stack = [initial]
        while stack:
            state = stack.pop()
            if state.idx not in visited:
                state.print()
                visited.add(state.idx)
                for _, _next in state._transitions.items():
                    stack.append(_next)

        state = initial
        for ch in s:
            next_state = state.get_transition(ch)
            if next_state:
                # print(f"[{state.idx}], {ch} -> [{next_state.idx}]")
                state = next_state
            else:
                # print(f"[{state.idx}], {ch} -> None")
                return False

        return state.is_final()
          

class State:
    def __init__(self, idx):
        self.idx = idx
        self._transitions = {}
        self._final = False

    def add_transition(self, ch, state):
        print(f"State({self.idx}).add_transition({ch}, {state.idx})")
        if ch not in self._transitions:
            self._transitions[ch] = state
    
    def set_final(self):
        self._final = True

    def get_transition(self, ch):
        return self._transitions.get(ch, self._transitions.get(".", None))

    def is_final(self):
        return self._final

    def print(self):
        final_str = "*" if self._final else ""
        print(f"State[{self.idx}] {final_str}")
        for ch, s in self._transitions.items():
            print(f"\t({ch}) -> [{s.idx}]")

class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        # self.assertEqual(False, self.solution.isMatch("aa", "a"))
        # self.assertEqual(True, self.solution.isMatch("aa", "a*"))
        # self.assertEqual(True, self.solution.isMatch("ab", ".*"))
        # self.assertEqual(True, self.solution.isMatch("aab", "c*a*b"))
        # self.assertEqual(False, self.solution.isMatch("mississippi", "mis*is*p*"))
        # self.assertEqual(True, self.solution.isMatch("mississippi", "mis*is*ip*i"))
        # self.assertEqual(True, self.solution.isMatch("aaabbb", "a*b*"))
        # self.assertEqual(False, self.solution.isMatch("bbbaaa", "a*b*"))
        self.assertEqual(True, self.solution.isMatch("aaa", "a*a"))


if __name__ == '__main__':
    unittest.main()
