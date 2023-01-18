"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

Runtime: 26 ms
Memory: 13.9 MB
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/880578228/
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        j2z = {}
        for i in range(9, 26):
            j2z[str(i+1) + '#'] = chr(97 + i)

        a2i = {}
        for i in range(9):
            a2i[str(i + 1)] = chr(97 + i)

        for k, v in j2z.items():
            s = s.replace(k, v)

        for k, v in a2i.items():
            s = s.replace(k, v)

        return s


def main():
    s = "1326#"
    result = Solution().freqAlphabets(s)
    print(result)


if __name__ == '__main__':
    main()
