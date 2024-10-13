/*
Runtime:	2 ms
RT Beats:	53.48%
Memory: 	2.15 MB
Mem Beats:	33.15%
Submission:	https://leetcode.com/problems/roman-to-integer/submissions/1421179357/
*/

use std::collections::HashMap;

struct Solution {}

impl Solution {
    fn new() -> HashMap<char, i32> {
        let map = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]);

        map
    }

    pub fn roman_to_int(s: String) -> i32 {
        let mut total = 0;
        let mut current;
        let mut prev = 0;
        let map = Solution::new();


        for c in s.chars() {
            current = map[&c];
            if current > prev {
                total += current - (2 * prev);
            } else {
                total += current
            }
            prev = current
        }

        total
    }
}

fn main() {
    let s = "MCMXCIV".to_string();
    let result = Solution::roman_to_int(s);
    println!("{}", result);
}
