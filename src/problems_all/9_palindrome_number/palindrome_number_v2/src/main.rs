/*
Runtime:            2 ms
Beats:              48.32%
Memory:             2.26 MB
Beats:              23.07%
Submission:         https://leetcode.com/problems/palindrome-number/submissions/1480394030/
Time complexity:    O(log10 n)
Space complexity:   O(1)
Topics:             #math
Solved By:          #math
*/

struct Solution {}

impl Solution {
    pub fn is_palindrome(mut x: i32) -> bool {
        if x < 0 || (x % 10 == 0 && x != 0) {
            return false;
        }

        let mut rev = 0;
        let mut digit;
        while x > rev {
            digit = x % 10;
            rev = rev * 10 + digit;
            x /= 10;
        }

        x == rev || x == rev / 10
    }
}

fn main() {
    let n = 121;
    let result = Solution::is_palindrome(n);
    println!("{}", result);
}
