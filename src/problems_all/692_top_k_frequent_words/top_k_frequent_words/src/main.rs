/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.44 MB
Beats:              30.77%
Submission:         https://leetcode.com/problems/top-k-frequent-words/submissions/1477113039/
Time complexity:    `O(n log n + k log n)` = `O(n log n)`, assuming k is significantly smaller than n.
                    * Building the heap: O(n log n), where n is the number of words.
                    * Extracting the top k elements: O(k log n)
Space complexity:   O(n)
Topics:             #hash-table, #string, #trie, #sorting, #heap (Priority Queue), #bucket-sort, #counting
Solved By:          #heap
*/

use std::collections::{BinaryHeap, HashMap};

struct Solution {}

impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        let mut counter = HashMap::new();
        for word in words {
            *counter.entry(word).or_insert(0) += 1;
        }

        let mut heap = BinaryHeap::new();
        for (word, count) in counter {
            heap.push((-count, word));
            if heap.len() > k as usize {
                heap.pop();
            }
        }

        let mut result = Vec::new();
        while let Some((_, word)) = heap.pop() {
            result.push(word)
        }
        result.reverse();

        result
    }
}

fn main() {
    let words_vec = [
        "the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is",
    ]
    .map(|t| t.to_string());
    let words = Vec::from(words_vec);
    let k = 4;
    let result = Solution::top_k_frequent(words, k);
    println!("{:?}", result);
}
