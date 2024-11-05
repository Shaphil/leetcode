/*
Runtime:	0 ms
Beats:	    100.00%
Memory: 	2.12 MB
Beats:	    53.71%
Submission:	https://leetcode.com/problems/add-binary/submissions/1442906957/
Topics:     #math #string #bit-manipulation #simulation
*/

struct Solution {}

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut result = String::new();
        let mut carry = 0;
        let mut i = a.len();
        let mut j = b.len();

        while i > 0 || j > 0 || carry > 0 {
            if i > 0 {
                i -= 1;
                carry += a.chars().nth(i).unwrap() as u8 - '0' as u8;
            }
            if j > 0 {
                j -= 1;
                carry += b.chars().nth(j).unwrap() as u8 - '0' as u8;
            }
            result.push((carry % 2 + '0' as u8) as char);
            carry /= 2;
        }

        result.chars().rev().collect()
    }
}

fn main() {
    let a = "1010".to_string();
    let b = "1011".to_string();
    let result = Solution::add_binary(a, b);
    println!("{}", result);
}
