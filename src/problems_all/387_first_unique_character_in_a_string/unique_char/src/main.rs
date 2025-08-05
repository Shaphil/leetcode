/*
Runtime:            11 ms
Beats:              55.77%
Memory:             2.39 MB
Beats:              40.38%
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #hash-table, #string, #queue, #counting
Solved By:          #hash-table
Submission:         https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1724523458/
*/

use std::collections::HashMap;

struct Solution {}

fn counter(items: &str) -> HashMap<char, i32> {
    let mut counts = HashMap::new();
    for item in items.chars() {
        *counts.entry(item).or_insert(0) += 1;
    }
    counts
}

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let counter = counter(&s);

        for (i, c) in s.chars().enumerate() {
            if let Some(&count) = counter.get(&c) {
                if count == 1 {
                    return i as i32;
                }
            }
        }

        -1
    }
}

fn main() {
    let pos = Solution::first_uniq_char("loveleetcode".to_string());
    println!("{}", pos);
}
