/*
Runtime:            4 ms
Beats:              66.81%
Memory:             4.01 MB
Beats:              30.12%
Submission:         https://leetcode.com/problems/contains-duplicate/submissions/1484672157/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sorting
Solved By:          #hash-table
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let nums_set: HashSet<i32> = HashSet::from_iter(nums.clone().iter().cloned());
        nums.len() != nums_set.len()
    }
}

fn main() {
    let nums = Vec::from([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]);
    let result = Solution::contains_duplicate(nums);
    println!("{}", result);
}
