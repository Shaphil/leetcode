/*
Runtime:    0 ms
Beats:	    100.00%
Memory: 	2.32 MB
Beats:	    21.32%
Submission:	https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1460136764/
Topics:     #array, #two-pointers
Solved by:  #two-pointers
*/


struct Solution {}

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut slow = 0;
        for fast in 0..nums.len() {
            if nums[slow] != nums[fast] {
                slow += 1;
                nums[slow] = nums[fast];
            }
        }

        slow as i32 + 1
    }
}


fn main() {
    let mut nums = Vec::from([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);
    let result = Solution::remove_duplicates(&mut nums);
    println!("{}", result);
}
