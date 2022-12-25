"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Runtime: 41 ms
Memory: 13.8 MB
"""

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        highest = max(salary)
        lowest = min(salary)
        average = (sum(salary) - highest - lowest) / (len(salary) - 2)
        return average


def main():
    salary = [4000, 3000, 1000, 2000]
    avg = Solution().average(salary)
    print(avg)


if __name__ == '__main__':
    main()
