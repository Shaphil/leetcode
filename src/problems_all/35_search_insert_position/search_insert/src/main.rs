/*
Runtime:	0 ms
RT Beats:	100.00%
Memory: 	2.30 MB
Mem Beats:	14.46%
Submission:	https://leetcode.com/problems/search-insert-position/submissions/1439175246/
*/

struct Solution {}

impl Solution {
    fn binary_search(arr: Vec<i32>, lo: i32, hi: i32, x: i32) -> i32 {
        if hi >= lo {
            let mid = ((hi + lo) / 2) as usize;

            if mid >= arr.len() {
                return -1;
            }

            if arr[mid] == x {
                mid as i32
            } else if arr[mid] > x {
                return Self::binary_search(arr, lo, (mid - 1) as i32, x);
            } else {
                return Self::binary_search(arr, (mid + 1) as i32, hi, x);
            }
        } else {
            -1
        }
    }

    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let len = nums.clone().len() as i32;
        let res = Self::binary_search(nums.clone(), 0, len, target);

        if res != -1 {
            res
        } else {
            for (i, v) in nums.iter().enumerate() {
                if v > &target {
                    return i as i32;
                }
            }

            nums.len() as i32
        }
    }
}

fn main() {
    let nums = Vec::from([1, 3, 5, 6]);
    let target = 7;

    let result = Solution::search_insert(nums, target);
    println!("{}", result);
}
