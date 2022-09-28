# class Solution:
#     def reverse(self, x: int) -> int:
#         min_val = -2 ** 31
#         max_val = 2 ** 31 - 1
#         is_negative = False
#         return_val = 0

#         if x < 0:
#             is_negative = True
#             x *= -1

#         x = str(x)
#         x = reversed(x)
#         x = ''.join(list(x))
#         x = int(x)

#         if is_negative:
#             x *= -1

#         if x >= min_val and x <= max_val:
#             return_val = x

#         return return_val


class Solution:
    def reverse(self, x: int) -> int:
        hi = 2 ** 31 - 1
        lo = -2 ** 31

        is_neg = False
        if x < 0:
            x *= -1
            is_neg = True

        s = list(str(x))
        s.reverse()
        r = int(''.join(s))

        if r > hi or r < lo:
            r = 0

        if is_neg:
            r *= -1

        return r


def solve():
    x = 120
    solution = Solution()
    print(solution.reverse(x))


if __name__ == '__main__':
    solve()
