/*
Runtime:            0 ms
Beats:              100.00%
Memory:             3.36 MB
Beats:              18.64%
Submission:         https://leetcode.com/problems/find-the-duplicate-number/submissions/1500816716/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #two-pointers, #binary-search, #bit-manipulation
Solved By:          #two-pointers
*/

struct Solution {}

impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut slow = nums[0] as usize;
        let mut fast = nums[0] as usize;

        loop {
            slow = nums[slow] as usize;
            fast = nums[nums[fast] as usize] as usize;
            if slow == fast {
                break;
            }
        }

        slow = nums[0] as usize;
        while slow != fast {
            slow = nums[slow] as usize;
            fast = nums[fast] as usize;
        }

        slow as i32
    }
}

fn main() {
    let nums = vec![1, 3, 4, 2, 2];
    let result = Solution::find_duplicate(nums);
    println!("{}", result);
}
