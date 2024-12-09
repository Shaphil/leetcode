/*
Runtime:            14 ms
Beats:              31.34%
Memory:             3.34 MB
Beats:              15.87%
Submission:         https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1474503879/
Time complexity:    O(n log k), where n = the number of elements in the input array; k = the desired k-th largest element
Space complexity:   O(k)
Topics:             #array, #divide-and-conquer, #sorting, #heap #priority-queue, #quickselect
Solved By:          #heap
*/

use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        for num in nums {
            heap.push(-num); // Negate to get a min-heap behavior
            if heap.len() > k as usize {
                heap.pop();
            }
        }
        -heap.pop().unwrap()
    }
}

fn main() {
    let nums = Vec::from([3, 2, 1, 5, 6, 4]);
    let k = 2;
    let result = Solution::find_kth_largest(nums, k);
    println!("{}", result);
}
