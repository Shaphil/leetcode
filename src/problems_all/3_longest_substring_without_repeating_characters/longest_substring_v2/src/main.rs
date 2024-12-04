/*
Runtime:            0 ms
Beats:	            100.00%
Memory: 	        2.42 MB
Beats:	            13.55%
Submission:	        https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1470440763/
Time complexity:    O(n)
Space Complexity:   O(k)
Topics:             #hash-table, #string, #sliding-window
Solved By:          #sliding-window
*/

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut last_seen = HashMap::new(); // Tracks the last position of each character
        let mut longest = 0;
        let mut left = 0;

        for (right, char) in s.chars().enumerate() {
            if let Some(&prev_index) = last_seen.get(&char) {
                // Update the left pointer to skip repeating characters
                left = left.max(prev_index + 1);
            }

            last_seen.insert(char, right); // Update the last seen position of the character
            longest = longest.max(right - left + 1);
        }

        longest as i32
    }
}

fn main() {
    let s = "abcabcbb".to_string();
    let result = Solution::length_of_longest_substring(s);
    println!("{}", result);
}
