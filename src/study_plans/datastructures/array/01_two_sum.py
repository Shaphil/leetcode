from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {val: pos for pos, val in enumerate(nums)}
        for pos, num in enumerate(nums):
            complement = target - num
            if complement in data and data[complement] != pos:
                return [pos, data[complement]]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 3]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)
