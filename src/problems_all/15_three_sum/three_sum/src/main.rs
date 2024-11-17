/*
Runtime:    22 ms
Beats:	    60.81%
Memory: 	4.01 MB
Beats:	    61.95%
Submission:	https://leetcode.com/problems/3sum/submissions/1455467059/
Topics:     #hash-table, #math, #two-pointers
Solved by:  #two-pointers
*/

struct Solution {}

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        nums.sort();

        for i in 0..(nums.len() - 2) {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let mut left = i + 1;
            let mut right = nums.len() - 1;

            while left < right {
                let sum = nums[i] + nums[left] + nums[right];
                if sum == 0 {
                    result.push(vec![nums[i], nums[left], nums[right]]);

                    // Skip duplicate numbers for left and right pointers
                    while left < right && nums[left] == nums[left + 1] {
                        left += 1;
                    }
                    while left < right && nums[right] == nums[right - 1] {
                        right -= 1;
                    }

                    left += 1;
                    right -= 1;
                } else if sum < 0 {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }

        result
    }
}

fn main() {
    let nums = Vec::from([-2, 0, 0, 2, 2]);
    let result = Solution::three_sum(nums);
    println!("{:?}", result);
}
