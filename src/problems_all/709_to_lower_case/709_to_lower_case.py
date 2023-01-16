"""
https://leetcode.com/problems/to-lower-case/description/

Runtime: 36 ms
Memory: 13.2 MB
https://leetcode.com/problems/to-lower-case/submissions/212516812/
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


def main():
    s = 'Hello'
    result = Solution().toLowerCase(s)
    print(result)


if __name__ == '__main__':
    main()
