from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break

        return prefix


if __name__ == '__main__':
    s = Solution()

    strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(s.longestCommonPrefix(strs))
