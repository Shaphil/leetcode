/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.46 MB
Beats:              17.65%
Submission:         https://leetcode.com/problems/teemo-attacking/submissions/1503166798/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #simulation
Solved By:          #simulation
*/

struct Solution {}

impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        if time_series.len() == 0 {
            return 0;
        }

        let mut total_duration = 0;
        for i in 0..time_series.len() - 1 {
            total_duration += i32::min(time_series[i + 1] - time_series[i], duration);
        }
        total_duration += duration;

        total_duration
    }
}

fn main() {
    let time_series = vec![1, 4];
    let duration = 2;
    let result = Solution::find_poisoned_duration(time_series, duration);
    println!("{}", result);
}
