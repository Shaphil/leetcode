/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.23 MB
Beats:              50.00%
Submission:         https://leetcode.com/problems/maximum-score-after-splitting-a-string/submissions/1495315452/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #string, #prefix-sum
Solved By:          #prefix-sum
*/

use std::cmp::max;

struct Solution {}

impl Solution {
    pub fn max_score(s: String) -> i32 {
        let total_ones = s.chars().filter(|&c| c == '1').count() as i32;
        let mut max_score = 0;
        let mut zeros_left = 0;
        let mut ones_right = total_ones;

        for (_, c) in s.chars().take(s.len() - 1).enumerate() {
            if c == '0' {
                zeros_left += 1;
            } else {
                ones_right -= 1;
            }
            max_score = max(max_score, zeros_left + ones_right);
        }

        max_score
    }
}

fn main() {
    let s = "011101".to_string();
    let result = Solution::max_score(s);
    println!("{}", result);
}
