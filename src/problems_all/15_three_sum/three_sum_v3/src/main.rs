/*
Runtime:    442 ms
Beats:	    22.88%
Memory: 	4.13 MB
Beats:	    34.80%
Submission:	https://leetcode.com/problems/3sum/submissions/1455606206/
Topics:     #hash-table, #math, #two-pointers
Solved by:  #hash-table
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort(); // Sort to simplify handling of duplicates
        let len = nums.len();
        let mut results = HashSet::new(); // Stores unique triplets

        for i in 0..len - 2 {
            if i > 0 && nums[i] == nums[i - 1] {
                continue; // Skip duplicate values for i
            }

            let mut seen = HashSet::new();
            for j in i + 1..len {
                let complement = -(nums[i] + nums[j]);
                if seen.contains(&complement) {
                    results.insert(vec![nums[i], complement, nums[j]]);
                }
                seen.insert(nums[j]); // Add current number to seen
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
