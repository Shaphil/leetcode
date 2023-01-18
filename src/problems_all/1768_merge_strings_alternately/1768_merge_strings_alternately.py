"""
https://leetcode.com/problems/merge-strings-alternately/

Runtime: 38 ms
Memory: 14 MB
https://leetcode.com/problems/merge-strings-alternately/submissions/879289507/
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = word1 if len(word1) < len(word2) else word2
        larger = word1 if len(word1) > len(word2) else word2
        merged = ''

        for i in range(len(shorter)):
            merged += word1[i]
            merged += word2[i]

        merged += larger[len(shorter):]
        return merged


def main():
    word1 = "abcd"
    word2 = "pq"
    result = Solution().mergeAlternately(word1, word2)
    print(result)


if __name__ == '__main__':
    main()
