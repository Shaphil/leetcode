/*
Runtime:            6 ms
Beats:              32.53%
Memory:             3.11 MB
Beats:              86.75%
Submission:         https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1506278667/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table
Solved By:          #hash-set
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let x: HashSet<i32> = (1..=nums.len() as i32).collect();
        let nums_set: HashSet<i32> = nums.into_iter().collect();
        let diff: Vec<i32> = x.difference(&nums_set).cloned().collect();

        diff
    }
}

fn main() {
    let nums = vec![4, 3, 2, 7, 8, 2, 3, 1];
    let result = Solution::find_disappeared_numbers(nums);
    println!("{:?}", result);
}
