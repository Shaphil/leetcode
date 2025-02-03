/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.24 MB
Beats:              50.00%
Submission:         https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/submissions/1530002091/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array
Solved By:          #array
*/

struct Solution {}

impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut longest = 1;
        let mut increasing = 1;
        let mut decreasing = 1;

        if n == 1 {
            return 1;
        }

        for i in 1..n {
            if nums[i] > nums[i - 1] {
                increasing += 1;
                decreasing = 1;
            } else if nums[i] < nums[i - 1] {
                decreasing += 1;
                increasing = 1;
            } else {
                increasing = 1;
                decreasing = 1;
            }

            longest = i32::max(longest, i32::max(increasing, decreasing));
        }

        longest
    }
}

fn main() {
    let nums = vec![1, 4, 3, 3, 2];
    let result = Solution::longest_monotonic_subarray(nums);
    println!("{}", result);
}
