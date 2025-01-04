/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.47 MB
Beats:              26.34%
Submission:         https://leetcode.com/problems/missing-number/submissions/1497593563/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #hash-table, #math, #binary-search, #bit-manipulation, #sorting
Solved By:          #math
*/

struct Solution {}

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let expected = (n * (n + 1)) / 2;
        let actual: i32 = nums.iter().sum();

        (expected - actual as usize) as i32
    }
}

fn main() {
    let nums = vec![3, 0, 1];
    let result = Solution::missing_number(nums);
    println!("{}", result);
}
