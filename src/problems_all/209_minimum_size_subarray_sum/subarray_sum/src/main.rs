/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.95 MB
Beats:              82.84%
Submission:         https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1498591405/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #binary-search, #sliding-window, #prefix-sum
Solved By:          #sliding-window
*/

use std::cmp::min;

struct Solution {}

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut min_length = i32::MAX;
        let mut current_sum = 0;
        let mut start = 0;

        for end in 0..n {
            current_sum += nums[end];
            while current_sum >= target {
                min_length = min(min_length, end as i32 - start + 1);
                current_sum -= nums[start as usize];
                start += 1;
            }
        }

        if min_length != i32::MAX {
            min_length
        } else {
            0
        }
    }
}

fn main() {
    let target = 7;
    let nums = vec![2, 3, 1, 2, 4, 3];
    let result = Solution::min_sub_array_len(target, nums);
    println!("{}", result);
}
