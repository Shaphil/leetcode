from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i in arr:
            if i + 1 in arr:
                count += 1

        return count


if __name__ == "__main__":
    arr = [1, 3, 2, 3, 5, 0]
    result = Solution().countElements(arr)
    print(result)
