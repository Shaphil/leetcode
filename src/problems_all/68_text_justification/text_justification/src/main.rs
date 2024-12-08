/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.28 MB
Beats:              37.29%
Submission:         https://leetcode.com/problems/text-justification/submissions/1473646387/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #string, #simulation
Solved By:          #simulation
*/

struct Solution {}

impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        let mut result = Vec::new();
        let mut current_line: Vec<String> = Vec::new();
        let mut current_length = 0;

        for word in words {
            if current_length + word.len() + current_line.len() > max_width as usize {
                // Distribute spaces
                for i in 0..(max_width as usize - current_length) {
                    let idx = i % ((current_line.len() - 1).max(1));
                    current_line[idx].push(' ');
                }

                // Join the line and add to result
                result.push(current_line.join(""));
                current_line = Vec::new();
                current_length = 0;
            }

            // Add the word to the current line
            current_line.push(word.clone());
            current_length += word.len();
        }

        // Handle the last line (left-justified)
        let last_line = current_line.join(" ");
        let padded_last_line =
            last_line.clone() + &" ".repeat(max_width as usize - last_line.len());
        result.push(padded_last_line);

        result
    }
}

fn main() {
    let words_arr = [
        "This",
        "is",
        "an",
        "example",
        "of",
        "text",
        "justification.",
    ];
    let words: Vec<String> = words_arr.iter().map(|&s| s.to_string()).collect();
    let max_width = 16;
    let result = Solution::full_justify(words, max_width);
    println!("{:?}", result);
}
