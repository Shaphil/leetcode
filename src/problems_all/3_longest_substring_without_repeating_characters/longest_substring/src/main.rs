/*
Runtime:            149 ms
Beats:	            10.71%
Memory: 	        2.43 MB
Beats:	            13.55%
Submission:	        https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1470428806/
Time complexity:    O(n^2)
Topics:             #hash-table, #string, #sliding-window
Solved By:          #sliding-window
*/

use std::cmp::max;
use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut chars_seen = HashSet::new();
        let mut longest = 0;

        let mut left = 0;
        for (right, char) in s.chars().enumerate() {
            while chars_seen.contains(&char) {
                chars_seen.remove(&s.chars().nth(left).unwrap());
                left += 1;
            }

            chars_seen.insert(char);
            longest = max(longest, right - left + 1);
        }

        longest as i32
    }
}

fn main() {
    let s = "abcabcbb".to_string();
    let result = Solution::length_of_longest_substring(s);
    println!("{}", result);
}
