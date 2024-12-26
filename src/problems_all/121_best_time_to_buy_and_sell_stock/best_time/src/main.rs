/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.97 MB
Beats:              87.63%
Submission:         https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1489006245/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #dynamic-programming
Solved By:          #array
*/

struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut best_time = 0;
        let mut smallest = prices[0];

        for (i, price) in prices.iter().enumerate() {
            if price < &smallest {
                smallest = *price;
            }

            let profit = *price - smallest;
            best_time = i32::max(best_time, profit);

            if i == prices.len() - 1 {
                return i32::max(best_time, 0);
            }
        }

        best_time
    }
}

fn main() {
    let prices = Vec::from([7, 1, 5, 3, 6, 4]);
    let best = Solution::max_profit(prices);
    println!("{}", best);
}
