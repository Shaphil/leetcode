/*
Runtime:            9 ms
Beats:              24.10%
Memory:             3.45 MB
Beats:              85.54%
Submission:         https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1506344232/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table
Solved By:          #hash-set
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let n: HashSet<i32> = nums.clone().into_iter().collect();
        let mut res = Vec::new();
        for i in 1..nums.len() + 1 {
            if !n.contains(&(i as i32)) {
                res.push(i as i32);
            }
        }

        res
    }
}

fn main() {
    let nums = vec![4, 3, 2, 7, 8, 2, 3, 1];
    let result = Solution::find_disappeared_numbers(nums);
    println!("{:?}", result);
}
