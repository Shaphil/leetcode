/*
Runtime:    435 ms
Beats:	    24.18%
Memory: 	4.99 MB
Beats:	    5.07%
Submission:	https://leetcode.com/problems/3sum/submissions/1455599190/
Topics:     #hash-table, #math, #two-pointers
Solved by:  #hash-table
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let len = nums.len();
        nums.sort(); // Sort the input to simplify triplet finding
        let mut results = HashSet::new(); // To store unique triplets

        for i in 0..len - 2 {
            if i > 0 && nums[i] == nums[i - 1] {
                continue; // Skip duplicates for the first number
            }

            let mut seen = HashSet::new(); // Tracks elements seen in the current loop
            for j in i + 1..len {
                let complement = -(nums[i] + nums[j]);
                if seen.contains(&complement) {
                    results.insert(vec![nums[i], complement, nums[j]]);
                } else {
                    seen.insert(nums[j]);
                }
            }
        }

        results.into_iter().collect()
    }
}


fn main() {
    let nums = Vec::from([-2, 0, 0, 2, 2]);
    let result = Solution::three_sum(nums);
    println!("{:?}", result);
}
