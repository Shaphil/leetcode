"""
https://leetcode.com/problems/happy-number/description/

Runtime: 36 ms
Memory: 14 MB
https://leetcode.com/problems/happy-number/submissions/318642685/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            seq = []
            while True:
                nums = [(int(x) ** 2) for x in str(n)]
                if nums in seq:
                    return False
                else:
                    seq.append(nums)

                total = sum(nums)
                n = total
                if total == 1:
                    return True

            return False


def main():
    n = 19
    result = Solution().isHappy(n)
    print(result)


if __name__ == '__main__':
    main()
