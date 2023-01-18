"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

Runtime: 64 ms
Memory: 14 MB
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/submissions/880424346/
"""


from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda x: bin(x).count('1'))


def main():
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    result = Solution().sortByBits(arr)
    print(result)


if __name__ == '__main__':
    main()
