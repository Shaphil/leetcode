from typing import List
from collections import deque


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = deque()
        for num in nums:
            if num % 2 == 0:
                res.appendleft(num)
            else:
                res.append(num)

        return list(res)


if __name__ == '__main__':
    nums = [3, 1, 2, 4]
    solution = Solution().sortArrayByParity(nums)
    print(solution)
