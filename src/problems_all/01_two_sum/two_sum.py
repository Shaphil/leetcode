"""
Runtime:    54 ms
Memory:     17.72 MB
Submission: https://leetcode.com/problems/two-sum/submissions/1382153444/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Create an empty dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i  # Store the current number and its index

        # If no valid solution found, return an empty list
        return []


if __name__ == '__main__':
    target = 9
    nums = [2, 7, 11, 15]
    solution = Solution().twoSum(nums, target)
    print(solution)
