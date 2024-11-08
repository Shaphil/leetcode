/*
Runtime:    0 ms
Beats:	    100.00%
Memory: 	2.16 MB
Beats:	    25.19%
Submission:	https://leetcode.com/problems/happy-number/submissions/1446794719/
Topics:     #hash-table, #math, #two-pointers
Solved by:  #hash-table
*/


use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut seen = HashSet::new();
        let mut num = n;

        while !seen.contains(&num) {
            seen.insert(num);
            num = Self::square_sum(num);

            if num == 1 {
                return true;
            }
        }

        false
    }

    fn square_sum(n: i32) -> i32 {
        let mut sum = 0;
        let mut x = n;
        while x > 0 {
            let digit = x % 10;
            sum += digit * digit;
            x /= 10;
        }
        sum
    }
}

fn main() {
    let n = 19;
    let result = Solution::is_happy(n);
    println!("{}", result);
}