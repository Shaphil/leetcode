"""
Runtime:            50 ms
Beats:              19.17%
Memory:             30.74 MB
Beats:              56.89%
Submission:         https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1506311072/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #hash-table
Solved By:          #array
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1  # Adjust for 0-based indexing
            nums[index] = -abs(nums[index])  # Mark the number as seen

        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)  # Adjust for 0-based indexing

        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDisappearedNumbers(nums)
    print(result)
