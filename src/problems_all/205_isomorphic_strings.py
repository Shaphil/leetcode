"""
https://leetcode.com/problems/isomorphic-strings/
WA
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for i, j in zip(s, t):
            if i in map and map[i] != j:
                return False
            else:
                map[i] = j

        return True


def solve():
    s = "badc"
    t = "baba"
    solution = Solution()
    print(solution.isIsomorphic(s, t))


if __name__ == '__main__':
    solve()
