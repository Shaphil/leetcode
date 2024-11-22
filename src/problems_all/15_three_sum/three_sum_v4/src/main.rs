/*
Runtime:    21 ms
Beats:	    65.36%
Memory: 	4.26 MB
Beats:	    22.64%
Submission:	https://leetcode.com/problems/3sum/submissions/1455612371/
Topics:     #hash-table, #math, #two-pointers
Solved by:  #hash-table, #two-pointers
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort(); // Sort the array
        let mut results = HashSet::new(); // To store unique triplets
        let len = nums.len();

        for i in 0..len - 2 {
            if i > 0 && nums[i] == nums[i - 1] {
                continue; // Skip duplicate values for i
            }

            let (mut left, mut right) = (i + 1, len - 1);
            while left < right {
                let sum = nums[i] + nums[left] + nums[right];
                if sum == 0 {
                    results.insert(vec![nums[i], nums[left], nums[right]]);
                    left += 1;
                    right -= 1;

                    // Skip duplicates for left pointer
                    while left < right && nums[left] == nums[left - 1] {
                        left += 1;
                    }

                    // Skip duplicates for right pointer
                    while left < right && nums[right] == nums[right + 1] {
                        right -= 1;
                    }
                } else if sum < 0 {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }

        results.into_iter().collect()
    }
}


fn main() {
    let nums = Vec::from([0, 0, 0]);
    let result = Solution::three_sum(nums);
    println!("{:?}", result);
}