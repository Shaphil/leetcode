/*
Runtime:            0 ms
Beats:              100.00%
Memory:             3.08 MB
Beats:              40.12%
Submission:         https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1489010428/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #dynamic-programming
Solved By:          #array
*/

struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = i32::MAX;
        let mut max_profit = 0;

        for price in prices {
            if price < min_price {
                min_price = price;
            } else if price - min_price > max_profit {
                max_profit = price - min_price;
            }
        }

        max_profit
    }
}

fn main() {
    let prices = Vec::from([7, 1, 5, 3, 6, 4]);
    let best = Solution::max_profit(prices);
    println!("{}", best);
}
