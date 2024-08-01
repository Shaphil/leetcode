fn main() {
    let jewels = String::from("aA");
    let stones = String::from("aAAbbbb");

    let count = Solution::num_jewels_in_stones(jewels, stones);
    println!("Count: {}", count);
}

struct Solution {}

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut count = 0;

        for j in jewels.chars() {
            for s in stones.chars() {
                if j == s {
                    count += 1;
                }
            }
        }

        count
    }
}