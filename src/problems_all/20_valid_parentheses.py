class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '{', '['}
        closing = {')', '}', ']'}
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        braces = []
        for c in s:
            if c in opening:
                braces.append(c)
            elif c in closing:
                if len(braces) == 0:
                    return False
                top = braces.pop()
                if c != pairs[top]:
                    return False

        return True if len(braces) == 0 else False


def solve():
    s = input()
    solution = Solution()
    print(solution.isValid(s))


if __name__ == '__main__':
    solve()
