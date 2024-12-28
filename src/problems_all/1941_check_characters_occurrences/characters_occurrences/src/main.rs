/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.25 MB
Beats:              57.14%
Submission:         https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/submissions/1490770119/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #hash-table, #string, #counting
Solved By:          #hash-set, #counting
*/

use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    pub fn are_occurrences_equal(s: String) -> bool {
        let mut counter = HashMap::new();
        for c in s.chars() {
            *counter.entry(c).or_insert(0) += 1;
        }

        let mut values_count = HashSet::new();
        for (_, i) in counter {
            values_count.insert(i);
        }

        values_count.len() == 1
    }
}

fn main() {
    let s = "aaabb".to_string();
    let result = Solution::are_occurrences_equal(s);
    println!("{}", result);
}
