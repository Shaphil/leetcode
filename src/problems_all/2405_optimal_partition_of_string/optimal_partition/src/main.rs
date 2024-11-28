/*
Runtime:    11 ms
Beats:	    36.84%
Memory: 	2.61 MB
Beats:	    14.29%
Submission:	https://leetcode.com/problems/optimal-partition-of-string/submissions/1465329332/
Topics:     #hash-table, #string, #greedy
Solved By:  #hash-table
*/

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn partition_string(s: String) -> i32 {
        let mut freq = HashMap::new();
        let mut partitions = 0;

        for c in s.chars() {
            let count = freq.entry(c).or_insert(0);
            *count += 1;

            if *count > 1 {
                partitions += 1;
                freq.clear();
                *freq.entry(c).or_insert(0) = 1;
            }
        }

        partitions + 1
    }
}

fn main() {
    let s = "abacaba".to_string();
    let result = Solution::partition_string(s);
    println!("{}", result);
}
