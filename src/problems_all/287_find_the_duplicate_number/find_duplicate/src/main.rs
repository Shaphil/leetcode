/*
Runtime:            24 ms
Beats:              5.08%
Memory:             3.40 MB
Beats:              13.56%
Submission:         https://leetcode.com/problems/find-the-duplicate-number/submissions/1500805541/
Time complexity:    O(n log n)
Space complexity:   O(1)
Topics:             #array, #two-pointers, #binary-search, #bit-manipulation
Solved By:          #two-pointers
*/

struct Solution {}

impl Solution {
    pub fn find_duplicate(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut prev = nums[0];
        let mut current;

        for i in 1..nums.len() {
            current = nums[i];
            if prev == current {
                return current;
            }
            prev = current;
        }
        0
    }
}

fn main() {
    let nums = vec![1, 3, 4, 2, 2];
    let result = Solution::find_duplicate(nums);
    println!("{}", result);
}
