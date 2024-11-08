/*
Runtime:    0 ms
Beats:	    100.00%
Memory: 	2.16 MB
Beats:	    25.19%
Submission:	https://leetcode.com/problems/happy-number/submissions/1446762758/
Solution:   https://leetcode.com/problems/happy-number/solutions/56917/my-solution-in-c-o-1-space-and-no-magic-math-property-involved/
Topics:     #hash-table, #math, #two-pointers
Solved by:  #two-pointers
*/

struct Solution {}

impl Solution {
    fn digit_square_sum(mut n: i32) -> i32 {
        let mut digit: i32;
        let mut sum = 0;

        while n > 0 {
            digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        sum
    }

    pub fn is_happy(n: i32) -> bool {
        let mut slow = n;
        let mut fast = n;
        loop {
            slow = Self::digit_square_sum(slow);
            fast = Self::digit_square_sum(fast);
            fast = Self::digit_square_sum(fast);
            if slow == fast {
                break;
            }
        }

        if slow == 1 {
            return true;
        }
        false
    }
}

fn main() {
    let n = 19;
    let result = Solution::is_happy(n);
    println!("{}", result);
}
