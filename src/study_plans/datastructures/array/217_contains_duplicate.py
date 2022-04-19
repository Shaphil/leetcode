from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(nums) != len(num_set)


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = Solution().containsDuplicate(nums)
    print(result)