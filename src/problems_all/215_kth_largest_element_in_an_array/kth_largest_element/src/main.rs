/*
Runtime:            16 ms
Beats:              19.40%
Memory:             3.32 MB
Beats:              15.87%
Submission:         https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1474424528/
Time complexity:    O(n log n)
Space complexity:   O(n)
Topics:             #array, #divide-and-conquer, #sorting, #heap #priority-queue, #quickselect
Solved By:          #sorting
*/

struct Solution {}

impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_by(|a, b| b.cmp(a));
        nums[k as usize - 1]
    }
}

fn main() {
    let nums = Vec::from([3, 2, 1, 5, 6, 4]);
    let k = 2;
    let result = Solution::find_kth_largest(nums, k);
    println!("{}", result);
}
