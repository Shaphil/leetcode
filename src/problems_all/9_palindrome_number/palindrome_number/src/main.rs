/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.16 MB
Beats:              57.52%
Submission:         https://leetcode.com/problems/palindrome-number/submissions/1480387343/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
*/

struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s = x.to_string();
        let inv = s.chars().rev().collect::<String>();

        s == inv
    }
}

fn main() {
    let n = -121;
    let result = Solution::is_palindrome(n);
    println!("{}", result);
}
