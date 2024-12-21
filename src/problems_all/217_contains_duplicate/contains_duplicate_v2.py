"""
Runtime:            3 ms
Beats:              98.38%
Memory:             31.54 MB
Beats:              23.44%
Submission:         https://leetcode.com/problems/contains-duplicate/submissions/1484689034/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sorting
Solved By:          #hash-set
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


def main():
    nums = [1, 2, 3, 4]
    result = Solution().containsDuplicate(nums)
    print(result)


if __name__ == '__main__':
    main()
