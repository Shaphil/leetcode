/*
Runtime:    15 ms
Beats:	    15.79%
Memory: 	2.62 MB
Beats:	    14.29%
Submission:	https://leetcode.com/problems/optimal-partition-of-string/submissions/1465333803/
Topics:     #hash-table, #string, #greedy
Solved By:  #greedy
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn partition_string(s: String) -> i32 {
        let mut seen = HashSet::new();
        let mut partitions = 1;

        for char in s.chars() {
            if seen.contains(&char) {
                partitions += 1;
                seen.clear();
            }
            seen.insert(char);
        }

        partitions
    }
}

fn main() {
    let s = "abacaba".to_string();
    let result = Solution::partition_string(s);
    println!("{}", result);
}
