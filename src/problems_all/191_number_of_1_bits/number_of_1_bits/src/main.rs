/*
Runtime:    2 ms
Memory:     2.15 MB
Submission: https://leetcode.com/problems/number-of-1-bits/submissions/1348242317/
*/

fn main() {
    let result = Solution::hamming_weight(2147483647);
    println!("{}", result);
}

struct Solution {}

impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        let bin = format!("{n:b}");
        let mut count = 0;
        for c in bin.chars() {
            if c == '1' {
                count += 1;
            }
        }

        count
    }
}