/*
Runtime:            3 ms
Beats:              29.51%
Memory:             3.21 MB
Beats:              22.13%
Submission:         https://leetcode.com/problems/first-missing-positive/submissions/1506605258/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #hash-table
Solved By:          #array
*/

struct Solution {}

impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();

        for i in 0..n {
            while nums[i] > 0 && nums[i] as usize <= n && nums[nums[i] as usize - 1] != nums[i] {
                let j = nums[i] as usize - 1;
                nums.swap(i, j);
            }
        }

        for i in 0..n {
            if nums[i] != (i + 1) as i32 {
                return (i + 1) as i32;
            }
        }

        (n + 1) as i32
    }
}

fn main() {
    let nums = vec![7, 8, 9, 11, 12];
    let result = Solution::first_missing_positive(nums);
    println!("{}", result);
}
