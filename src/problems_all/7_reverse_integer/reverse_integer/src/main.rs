/*
Runtime:            3 ms
Beats:              36.49%
Memory:             2.33 MB
Beats:              22.27%
Submission:         https://leetcode.com/problems/reverse-integer/submissions/1485599909/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
*/

struct Solution {}

impl Solution {
    pub fn reverse(mut x: i32) -> i32 {
        if x == 0 {
            return 0;
        }

        let is_negative = x < 0;
        x = x.abs();

        let s = x.to_string();
        let reversed = s.chars().rev().collect::<String>();
        let mut val: i32 = reversed.parse().unwrap_or_else(|_| 0);

        if is_negative {
            val *= -1;
        }

        val
    }
}

fn main() {
    let x = 120;
    let result = Solution::reverse(x);
    println!("{}", result);
}
