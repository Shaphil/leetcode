/*
Runtime:    30 ms
Memory:     2.69 MB
Submission: https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1410531920/
*/

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let mut total = 0;
        let allowed: HashSet<char> = allowed.chars().collect();

        for word in words {
            let w: HashSet<char> = word.chars().collect();
            if w.is_subset(&allowed) {
                total += 1;
            }
        }

        total
    }
}

fn main() {
    let allowed = String::from("ab");
    let words = ["ad", "bd", "aaab", "baa", "badab"]
        .iter()
        .map(|s| s.to_string())
        .collect::<Vec<String>>();

    let result = Solution::count_consistent_strings(allowed, words);
    println!("{}", result);
}

