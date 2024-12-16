/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.28 MB
Beats:              20.83%
Submission:         https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/1480304691/
Time complexity:    O(1)
Space complexity:   O(1)
Topics:             #math
Solved By:          #math
*/

struct Solution {}

impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        let hi_odds = if high % 2 == 0 { high / 2} else { (high + 1) / 2 };
        let lo_odds = if low % 2 == 0 {low / 2} else { (low - 1) / 2 };

        hi_odds - lo_odds
    }
}

fn main() {
    let low = 1;
    let high = 13;
    let result = Solution::count_odds(low, high);
    println!("{}", result);
}
