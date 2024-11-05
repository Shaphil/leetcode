"""
Runtime:    3 ms
Beats:      46.11%
Memory:     16.64 MB
Beats:      36.83%
Submission: https://leetcode.com/problems/add-binary/submissions/1441874056/
Topics:     #math #string #bit-manipulation #simulation
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            carry = total // 2
            result = str(total % 2) + result

        return result


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    result = Solution().addBinary(a, b)
    print(result)
