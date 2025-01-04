/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.28 MB
Beats:              49.42%
Submission:         https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1497819331/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #binary-search, #divide-and-conquer
Solved By:          #array
*/

struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> f64 {
        nums1.append(&mut nums2);
        nums1.sort();
        let total = nums1.len();

        if total % 2 == 1 {
            nums1[total / 2] as f64
        } else {
            let mid1 = nums1[total / 2 - 1] as f64;
            let mid2 = nums1[total / 2] as f64;
            (mid1 + mid2) / 2.0
        }
    }
}

fn main() {
    let nums1 = vec![1, 3];
    let nums2 = vec![2];
    let result = Solution::find_median_sorted_arrays(nums1, nums2);
    println!("{}", result);
}
