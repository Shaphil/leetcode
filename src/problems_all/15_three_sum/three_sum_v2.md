# Understanding the Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that
`nums[i] + nums[j] + nums[k] == 0`.

## Approach

1. Sort the Array
    * Sort the array in ascending order to efficiently find triplets.
2. Iterate and Fix the First Element:
    * Iterate through the array, fixing the first element `nums[i]`.
    * Skip duplicate values for the first element to avoid redundant triplets.
3. Two-Pointer Approach:
    * Initialize two pointers, `left` and `right`, to the indices after `i`.
    * Calculate the current sum: `current_sum = nums[i] + nums[left] + nums[right]`.
    * If `current_sum` is 0, we've found a triplet. Add it to the result and move both pointers to skip duplicates.
    * If `current_sum` is less than 0, increment left to increase the sum.
    * If `current_sum` is greater than 0, decrement right to decrease the sum.

## Python Implementation

```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate second numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate third numbers
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

## Key Points

* **Sorting:** Sorting the array allows us to efficiently use the two-pointer technique.
* **Skipping Duplicates:** By skipping duplicate numbers, we avoid redundant triplets and improve efficiency.
* **Two-Pointer Technique:** The `left` and `right` pointers effectively search for pairs that complement the fixed
  `nums[i]` to
  form a triplet.
* **Moving Pointers:** The pointers are adjusted based on the current sum to converge towards the target sum of 0.

This approach provides an efficient solution to the 3Sum problem by leveraging the two-pointer technique and handling
duplicates effectively.