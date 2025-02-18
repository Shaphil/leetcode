/*
Runtime:    0 ms
Beats:	    100.00%
Memory: 	2.16 MB
Beats:	    36.29%
Submission:	https://leetcode.com/problems/remove-element/submissions/1460271891/
Topics:     #array, #two-pointers
Solved by:  #two-pointers
*/


struct Solution {}

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut i = 0;
        for j in 0..nums.len() {
            if nums[j] != val {
                if i != j {
                    nums[i] = nums[j];
                }
                i += 1;
            }
        }

        i as i32
    }
}


fn main() {
    let mut nums = Vec::from([0, 1, 2, 2, 3, 0, 4, 2]);
    let val = 2;
    let result = Solution::remove_element(&mut nums, val);
    println!("{}", result);
}
