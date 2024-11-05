"""
Runtime:    0 ms
Beats:      100.00%
Memory:     16.54 MB
Beats:      70.45%
Submission: https://leetcode.com/problems/add-binary/submissions/1443778771/
Topics:     #math #string #bit-manipulation #simulation
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    result = Solution().addBinary(a, b)
    print(result)
