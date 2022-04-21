from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        sorted_list = []

        for _ in range(n):
            nums1.pop()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_list.append(nums1[i])
                i += 1
            else:
                sorted_list.append(nums2[j])
                j += 1

        if i < len(nums1):
            for x in range(i, len(nums1)):
                sorted_list.append(nums1[x])

        if j < len(nums2):
            for y in range(j, len(nums2)):
                sorted_list.append(nums2[y])

        for _ in range(n):
            nums1.append(0)

        for i in range(m + n):
            nums1[i] = sorted_list[i]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3

    nums2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1, m, nums2, n)
    print(nums1)
