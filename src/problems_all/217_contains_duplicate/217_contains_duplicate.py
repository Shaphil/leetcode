"""
https://leetcode.com/problems/contains-duplicate/description/

Runtime: 584 ms
Memory: 26.1 MB
https://leetcode.com/problems/contains-duplicate/submissions/678186913/
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
