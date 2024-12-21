/*
Runtime:            3 ms
Beats:              83.63%
Memory:             3.99 MB
Beats:              35.23%
Submission:         https://leetcode.com/problems/contains-duplicate/submissions/1484701131/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sorting
Solved By:          #hash-table
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();
        for num in nums {
            if seen.contains(&num) {
                return true;
            }
            seen.insert(num);
        }

        false
    }
}

fn main() {
    let nums = Vec::from([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]);
    let result = Solution::contains_duplicate(nums);
    println!("{}", result);
}
