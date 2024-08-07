/*
Runtime:    2 ms
Memory:     2.04 MB
Submission: https://leetcode.com/problems/number-of-1-bits/submissions/1348249030/
*/

fn main() {
    let result = Solution::hamming_weight(2147483647);
    println!("{}", result);
}

struct Solution {}

impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        let mut count = 0;
        let mut num = n;

        while num != 0 {
            count += num & 1;
            num >>= 1;
        }

        count
    }
}
