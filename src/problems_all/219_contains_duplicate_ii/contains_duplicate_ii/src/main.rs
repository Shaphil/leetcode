/*
Runtime:            12 ms
Beats:              35.80%
Memory:             6.86 MB
Beats:              19.14%
Submission:         https://leetcode.com/problems/contains-duplicate-ii/submissions/1492588735/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sliding-window
Solved By:          #hash-table
*/

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut mapping = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            if mapping.contains_key(num) && (i - mapping[num]) <= k as usize {
                return true;
            }
            mapping.insert(num, i);
        }

        false
    }
}

fn main() {
    let nums = vec![1, 2, 3, 1];
    let k = 3;
    let result = Solution::contains_nearby_duplicate(nums, k);
    println!("{}", result);
}
