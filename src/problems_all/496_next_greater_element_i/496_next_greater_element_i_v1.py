"""
https://leetcode.com/problems/next-greater-element-i/


Runtime: 38 ms
Memory: 14.2 MB

https://leetcode.com/problems/next-greater-element-i/submissions/871869744/
"""


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2items = {}
        for i, v in enumerate(nums2):
            n2items[v] = i

        result = []
        for i in nums1:
            idx = n2items[i]
            next_big = float('-inf')
            for j in range(idx, len(nums2)):
                if nums2[j] > next_big and nums2[j] > i:
                    next_big = nums2[j]
                    break

            if next_big == float('-inf'):
                result.append(-1)
            else:
                result.append(next_big)

        return result


def main():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = Solution().nextGreaterElement(nums1, nums2)
    print(result)


if __name__ == '__main__':
    main()
