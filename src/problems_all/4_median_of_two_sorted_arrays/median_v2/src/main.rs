
/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.35 MB
Beats:              17.72%
Submission:         https://leetcode.com/problems/median-of-two-sorted-arrays/
Time complexity:    O(log(min(m, n))), where, `m = len(nums1)` and `n = len(nums2)`
Space complexity:   O(1)
Topics:             #array, #binary-search, #divide-and-conquer
Solved By:          #binary-search
*/

struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (nums1, nums2) = if nums1.len() > nums2.len() {
            (nums2, nums1)
        } else {
            (nums1, nums2)
        };

        let x = nums1.len();
        let y = nums2.len();
        let mut lo = 0;
        let mut hi = x;

        while lo <= hi {
            let mid_x = (lo + hi) / 2;
            let mid_y = (x + y + 1) / 2 - mid_x;

            let max_left_x = if mid_x == 0 {
                i32::MIN
            } else {
                nums1[mid_x - 1]
            };

            let max_left_y = if mid_y == 0 {
                i32::MIN
            } else {
                nums2[mid_y - 1]
            };

            let min_right_x = if mid_x == x { i32::MAX } else { nums1[mid_x] };

            let min_right_y = if mid_y == y { i32::MAX } else { nums2[mid_y] };

            if max_left_x <= min_right_y && max_left_y <= min_right_x {
                return if (x + y) % 2 == 0 {
                    (f64::from(max_left_x.max(max_left_y))
                        + f64::from(min_right_x.min(min_right_y)))
                        / 2.0
                } else {
                    f64::from(max_left_x.max(max_left_y))
                };
            } else if max_left_x > min_right_y {
                hi = mid_x - 1;
            } else {
                lo = mid_x + 1;
            }
        }

        0.0
    }
}
fn main() {
    let nums1 = vec![1, 3];
    let nums2 = vec![2];
    let result = Solution::find_median_sorted_arrays(nums1, nums2);
    println!("{}", result);
}
