"""
Runtime:    0 ms
RT Beats:   100.00%
Memory:     16.74 MB
Mem Beats:  9.31%
Submission: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1432614139/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_hay = len(haystack)
        len_needle = len(needle)

        for i in range(len_hay - len_needle + 1):
            j = 0
            while j < len_needle and haystack[i + j] == needle[j]:
                j += 1
            if j == len_needle:
                return i

        return -1


if __name__ == '__main__':
    haystack = "leetcode"
    needle = "leeto"

    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)
