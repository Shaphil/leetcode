/*
Runtime:    28 ms
Memory:     2.20 MB
Submission: https://leetcode.com/problems/two-sum/submissions/1369111229/
*/

fn main() {
    let target = 9;
    let nums = Vec::from([2, 7, 11, 15]);
    let result = Solution::two_sum(nums, target);
    println!("{:?}", result);
}

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut first: i32 = 0;
        let mut last: i32 = 0;
        let mut res = Vec::new();

        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] + nums[j] == target {
                    first = i as i32;
                    last = j as i32;
                    break;
                }
            }
        }

        res.push(first);
        res.push(last);

        res
    }
}