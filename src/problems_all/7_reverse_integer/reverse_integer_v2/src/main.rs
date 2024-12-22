/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.32 MB
Beats:              22.27%
Submission:         https://leetcode.com/problems/reverse-integer/submissions/1485714179/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #math
Solved By:          #math
*/

struct Solution {}

impl Solution {
    pub fn reverse(mut x: i32) -> i32 {
        let min_val = i32::MIN;
        let max_val = i32::MAX;
        let mut reversed_num = 0;

        while x != 0 {
            let digit = x % 10;
            x /= 10;

            // Check for overflow before multiplying or adding
            if reversed_num > max_val / 10 || (reversed_num == max_val / 10 && digit > max_val % 10) {
                return 0;
            }
            if reversed_num < min_val / 10 || (reversed_num == min_val / 10 && digit < min_val % 10) {
                return 0;
            }

            reversed_num = reversed_num * 10 + digit;
        }

        reversed_num
    }
}


fn main() {
    let x = -120;
    let result = Solution::reverse(x);
    println!("{}", result);
}
