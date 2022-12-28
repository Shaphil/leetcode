"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Runtime: 47 ms
Memory: 14.1 MB
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/867002207/
"""


from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        is_prog = True

        for i in range(2, len(arr)):
            _diff = arr[i] - arr[i - 1]
            if _diff != diff:
                is_prog = False
                break

        return is_prog


def main():
    arr = [1, 5, 5]
    result = Solution().canMakeArithmeticProgression(arr)
    print(result)


if __name__ == '__main__':
    main()
