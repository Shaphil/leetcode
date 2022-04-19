from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        result = 0
        for key, val in counts.items():
            if val == 1:
                result = key

        return result


if __name__ == "__main__":
    l = [4, 1, 2, 1, 2]
    solution = Solution()
    num = solution.singleNumber(l)
    print(num)
