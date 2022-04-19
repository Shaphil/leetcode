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


if __name__ == "__main__":
    solution = Solution()
    happy = solution.isHappy(99)
    print(happy)
