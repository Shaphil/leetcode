class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp.reverse()
        rev = ' '.join(temp)
        return rev


def solve():
    s = "the sky is blue"
    solution = Solution()
    print(solution.reverseWords(s))


if __name__ == '__main__':
    solve()
