/*
Runtime:	0 ms
Beats:	    100.00%
Memory: 	2.14 MB
Beats:	    44.83%
Submission:	https://leetcode.com/problems/length-of-last-word/submissions/1440851635/
*/


struct Solution {}

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let words: Vec<&str> = s.trim().split(" ").collect();
        words.last().unwrap().len() as i32
    }
}


fn main() {
    let s = String::from("   word   ");
    let result = Solution::length_of_last_word(s);
    println!("{}", result);
}
