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
            
        seq = set()
        while True:
            nums = [(int(x) ** 2) for x in str(n)]
            total = sum(nums)
            
            if total == 1:
                return True

            if total in seq:
                return False
            
            seq.add(total)
            n = total

        return False


def main():
    n = 2
    result = Solution().isHappy(n)
    print(result)


if __name__ == '__main__':
    main()
