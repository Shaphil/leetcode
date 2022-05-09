from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        mappings = [data[digit] for digit in digits]
        prod = product(*mappings)
        result = [''.join(val) for val in prod if val]
        return result


def main():
    digits = ''
    result = Solution().letterCombinations(digits)
    print(result)


if __name__ == '__main__':
    main()
