/*
Runtime:            8 ms
Beats:              18.03%
Memory:             3.72 MB
Beats:              10.66%
Submission:         https://leetcode.com/problems/first-missing-positive/submissions/1506586176/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table
Solved By:          #hash-set
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        for num in nums {
            if num > 0 {
                seen.insert(num);
            }
        }

        for i in 1..(seen.len() + 2) {
            if !seen.contains(&(i as i32)) {
                return i as i32;
            }
        }

        (seen.len() + 1) as i32
    }
}

fn main() {
    let nums = vec![7, 8, 9, 11, 12];
    let result = Solution::first_missing_positive(nums);
    println!("{}", result);
}
