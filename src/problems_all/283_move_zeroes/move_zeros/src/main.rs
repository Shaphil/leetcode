/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.36 MB
Beats:              57.26%
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #two-pointers
Solved By:          #two-pointers
Submission:         https://leetcode.com/problems/move-zeroes/submissions/1790195651/
*/

struct Solution {}

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut left: usize = 0;
        let mut temp;
        for right in 0..nums.len() {
            if nums[right] != 0 {
                temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;

                left += 1;
            }
        }
    }
}

fn main() {
    let mut nums = Vec::from([0, 1, 0, 3, 12]);
    Solution::move_zeroes(&mut nums);
    println!("{:?}", nums);
}
