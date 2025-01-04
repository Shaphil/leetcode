/*
Runtime:            1 ms
Beats:              24.19%
Memory:             2.40 MB
Beats:              63.98%
Submission:         https://leetcode.com/problems/missing-number/submissions/1497582924/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #math, #binary-search, #bit-manipulation, #sorting
Solved By:          #hash-table (#hash-set)
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let expected: HashSet<i32> = (0..=nums.len() as i32).collect();
        let actual: HashSet<i32> = nums.into_iter().collect();
        let missing: Vec<i32> = expected.difference(&actual).cloned().collect();

        *missing.first().unwrap()
    }
}

fn main() {
    let nums = vec![3, 0, 1];
    let result = Solution::missing_number(nums);
    println!("{}", result);
}
