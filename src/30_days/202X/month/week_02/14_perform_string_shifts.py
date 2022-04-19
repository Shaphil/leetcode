from typing import List


class Solution:

    def flatten(self, val, s):
        flat = []
        if val > s:
            div, rem = val // s, val % s
            flat = [s] * div
            flat.append(rem)
        else:
            flat = [val]

        return flat

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ops = {0: 0, 1: 0}
        for move in shift:
            op, count = move
            ops[op] += count

        left = self.flatten(ops[0], len(s))
        right = self.flatten(ops[1], len(s))

        s = list(s)
        for l in left:
            s = s[l:] + s[:l]

        for r in right:
            s = s[-r:] + s[:-r]

        s = ''.join(s)

        return s


if __name__ == "__main__":
    s = "mecsk"
    shift = [[1, 4], [0, 5], [0, 4], [1, 1], [1, 5]]
    result = Solution().stringShift(s, shift)
    print(result)
