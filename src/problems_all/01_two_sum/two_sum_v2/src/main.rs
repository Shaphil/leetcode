/*
Runtime:    0 ms
Memory:     2.49 MB
Submission: https://leetcode.com/problems/two-sum/submissions/1382148292/
*/

use std::collections::HashMap;

fn main() {
    let target = 9;
    let nums = Vec::from([2, 7, 11, 15]);
    let result = Solution::two_sum(nums, target);
    println!("{:?}", result);
}


struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_to_index = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&index) = num_to_index.get(&complement) {
                return vec![index as i32, i as i32];
            }
            num_to_index.insert(num, i);
        }

        // No valid solution found, return an empty vector
        vec![]
    }
}
