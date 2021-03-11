from typing import List
import unittest

class Solution:
    LESS_THAN_TENS = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    LESS_THAN_TWENTIES = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    MULTIPLE_OF_TENS = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    POWERS_OF_THOU = ["One", "Thousand", "Million", "Billion"]

    def numberLessThanThousandToWords(self, num: int) -> List[str]:
        words = []
        digit_of_hundred = num // 100
        if digit_of_hundred > 0:
            words += [self.LESS_THAN_TENS[digit_of_hundred], "Hundred"]
        
        rest_of_hundred = num % 100
        if rest_of_hundred == 0:
            pass
        elif rest_of_hundred < 10:
            words += [self.LESS_THAN_TENS[rest_of_hundred]]
        elif rest_of_hundred < 20:
            words += [self.LESS_THAN_TWENTIES[rest_of_hundred-10]]
        else:
            digit_of_ten = rest_of_hundred // 10
            digit_of_one = rest_of_hundred % 10
            words += [self.MULTIPLE_OF_TENS[digit_of_ten]]
            if digit_of_one > 0:
                words += [self.LESS_THAN_TENS[digit_of_one]]
        
        return words

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.LESS_THAN_TENS[num]

        words = []
        for i in reversed(range(len(self.POWERS_OF_THOU))):
            power_of_thou = 10 ** (3*i)
            chunk = (num // power_of_thou) % (10 ** 3)
        
            if chunk > 0:
                chunk_words = self.numberLessThanThousandToWords(chunk)
                if i > 0:
                    chunk_words += [self.POWERS_OF_THOU[i]]
            else:
                chunk_words = []
            words += chunk_words

        return " ".join(words)

class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_solution(self):
        self.assertEqual("Zero", 
            self.solution.numberToWords(0))
        self.assertEqual("Twelve", 
            self.solution.numberToWords(12))
        self.assertEqual("One Hundred", 
            self.solution.numberToWords(100))
        self.assertEqual("One Hundred Twenty Three", 
            self.solution.numberToWords(123))
        self.assertEqual("Twelve Thousand Three Hundred Forty Five", 
            self.solution.numberToWords(12345))
        self.assertEqual("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven", 
            self.solution.numberToWords(1234567))
        self.assertEqual("One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One", 
            self.solution.numberToWords(1234567891))
        self.assertEqual("One Million Ten", 
            self.solution.numberToWords(1000010))


if __name__ == '__main__':
    unittest.main()
