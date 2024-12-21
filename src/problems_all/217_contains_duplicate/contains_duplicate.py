"""
Runtime:            584 ms
Beats:              5.04%
Memory:             26.1 MB
Beats:              95.39%
Submission:         https://leetcode.com/problems/contains-duplicate/submissions/678186913/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sorting
Solved By:          #hash-table
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(nums) != len(num_set)


def main():
    nums = [1, 2, 3, 1]
    result = Solution().containsDuplicate(nums)
    print(result)


if __name__ == '__main__':
    main()
