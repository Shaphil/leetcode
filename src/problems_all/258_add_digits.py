class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


if __name__ == "__main__":
    solution = Solution()
    num = 12345
    digit = solution.addDigits(num)
    print(digit)
