"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Runtime: 89 ms
Memory: 14.9 MB
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/877513125/
"""


from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_nums = []
        for i in range(1, len(arr) + 1, 2):
            odd_nums.append(i)

        odd_arrays = []
        for i in odd_nums:
            for j in range(len(arr)):
                if len(arr[j:j+i]) >= i:
                    odd_arrays += arr[j:j+i]

        return sum(odd_arrays)


def main():
    arr = [1, 2]
    result = Solution().sumOddLengthSubarrays(arr)
    print(result)


if __name__ == '__main__':
    main()
