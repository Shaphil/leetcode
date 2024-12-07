/*
Runtime:            31 ms
Beats:              60.00%
Memory:             2.43 MB
Beats:              64.71%
Submission:         https://leetcode.com/problems/burst-balloons/submissions/1472810336/
Time complexity:    O(n^3)
Space complexity:   O(n^2)
Topics:             #array, #dynamic-programming
Solved By:          #dynamic-programming
*/

use std::cmp::max;

struct Solution {}

impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        // Add virtual balloons with value 1 at the boundaries
        let mut one = vec![1];
        one.extend(nums.iter());
        one.push(1);

        let n = nums.len();
        let mut dp = vec![vec![0; n + 2]; n + 2]; // DP table for range (i, j)

        // Solve subproblems for ranges of increasing length
        for length in 2..=(n + 1) {
            // Length of the range
            for i in 0..=(n + 1 - length) {
                // Starting index
                let j = i + length; // Ending index

                // Try all possible k as the last balloon to burst in the range (i, j)
                for k in (i + 1)..j {
                    dp[i][j] = max(dp[i][j], dp[i][k] + one[i] * one[k] * one[j] + dp[k][j]);
                }
            }
        }

        dp[0][n + 1] // Maximum coins for the full range
    }
}

fn main() {
    let nums = Vec::from([3, 1, 5, 8]);
    let result = Solution::max_coins(nums);
    println!("{}", result);
}
