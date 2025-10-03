/*
Runtime:            2 ms
Beats:              20.64%
Memory:             2.30 MB
Beats:              80.56%
Submission:         https://leetcode.com/problems/valid-anagram/submissions/1790103864/
Time complexity:    O(m + n)
Space complexity:   O(1)
Topics:             #hash-table, #string, #sorting
Solved By:          #hash-table
*/

use std::collections::HashMap;

fn counter(s: String) -> HashMap<char, usize> {
    let mut count: HashMap<char, usize> = HashMap::new();
    for c in s.chars() {
        *count.entry(c).or_insert(0) += 1;
    }

    count
}

struct Solution {}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        counter(s) == counter(t)
    }
}

fn main() {
    let s = String::from("anagram");
    let t = String::from("nagaram");
    let result = Solution::is_anagram(s, t);
    println!("{:?}", result);
}
