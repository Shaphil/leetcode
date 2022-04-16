from typing import List


class Solution:
    # def countBits(self, n: int) -> List[int]:
    #     bits = []
    #     for i in range(n + 1):
    #         binary = bin(i)[2:]
    #         bit = sum(list(map(int, list(binary))))
    #         bits.append(bit)

    #     return bits

    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n + 1):
            binary = bin(i)[2:]
            bit = len(binary.replace('0', ''))
            bits.append(bit)
        
        return bits


if __name__ == "__main__":
    n = 5
    solution = Solution()
    bits = solution.countBits(n)
    print(bits)
