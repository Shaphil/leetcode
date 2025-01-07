/*
Runtime:            0 ms
Beats:              100.00%
Memory:             3.28 MB
Beats:              38.83%
Submission:         https://leetcode.com/problems/merge-intervals/submissions/1500883727/
Time complexity:    O(n log n)
Space complexity:   O(n)
Topics:             #array, #sorting
Solved By:          #sorting
*/

struct Solution {}

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by(|x, y| x[0].cmp(&y[0]));
        let mut merged = vec![intervals[0].clone()];

        for i in 1..intervals.len() {
            let start = intervals[i][0];
            let end = intervals[i][1];
            let last = merged.last_mut().unwrap();

            if start <= last[1] {
                last[1] = std::cmp::max(last[1], end);
            } else {
                merged.push(vec![start, end]);
            }
        }

        merged
    }
}

fn main() {
    let intervals = vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]];
    let result = Solution::merge(intervals);
    println!("{:?}", result);
}
