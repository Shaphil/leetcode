/*
Runtime:            57 ms
Beats:	            100.00%
Memory: 	        3.65 MB
Beats:	            36.29%
Submission:         https://leetcode.com/problems/minimum-time-to-complete-trips/submissions/1471159015/
Time complexity:    O(n * log(m)), where, n = len(time) and m = totalTrips * max(time)
Space Complexity:   O(1)
Topics:             #array, #binary-search
Solved by:          #binary-search
*/

struct Solution {}

impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        let mut left: i64 = 1;
        let mut right: i64 = *time.iter().max().unwrap_or(&0) as i64 * total_trips as i64;

        while right > left {
            let mid = left + (right - left) / 2;

            let mut sum: i64 = 0;
            for t in time.iter() {
                sum += mid / *t as i64;
            }

            if sum >= total_trips as i64 {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left
    }
}

fn main() {
    let time = Vec::from([1, 2, 3]);
    let total_trips = 5;
    let result = Solution::minimum_time(time, total_trips);
    println!("{}", result);
}
