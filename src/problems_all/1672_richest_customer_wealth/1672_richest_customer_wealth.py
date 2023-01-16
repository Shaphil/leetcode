"""
https://leetcode.com/problems/richest-customer-wealth/

Runtime: 57 ms
Memory: 14 MB
https://leetcode.com/problems/richest-customer-wealth/submissions/879080274/
"""


from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = float('-inf')
        for account in accounts:
            total = sum(account)
            if total > max_wealth:
                max_wealth = total

        return max_wealth


def main():
    accounts = [[1, 5], [7, 3], [3, 5]]
    result = Solution().maximumWealth(accounts)
    print(result)


if __name__ == '__main__':
    main()
