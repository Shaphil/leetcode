/*
Runtime:            29 ms
Beats:              91.67%
Memory:             30.01 MB
Beats:              5.05%
Submission:         https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1475422041/
Time complexity:    Insert: O(1), O(n) worst case; Remove: O(1), O(n) worst case; getRandom: O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #math, #design, #randomized
Solved By:          #hash-table
*/

use rand::Rng;
use std::collections::HashMap;

struct RandomizedSet {
    values: Vec<i32>,             // List to store the values
    indices: HashMap<i32, usize>, // Map to store value -> index mapping
}

impl RandomizedSet {
    fn new() -> Self {
        RandomizedSet {
            values: Vec::new(),
            indices: HashMap::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if self.indices.contains_key(&val) {
            return false; // Value already exists
        }
        // Add the value to the end of the list and record its index
        self.indices.insert(val, self.values.len());
        self.values.push(val);
        true
    }

    fn remove(&mut self, val: i32) -> bool {
        if let Some(&index_to_remove) = self.indices.get(&val) {
            let last_value = self.values[self.values.len() - 1];

            // Move the last element to the position of the element to remove
            self.values[index_to_remove] = last_value;
            self.indices.insert(last_value, index_to_remove);

            // Remove the last element from the list
            self.values.pop();
            self.indices.remove(&val);

            true
        } else {
            false // Value not found
        }
    }

    fn get_random(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let random_index = rng.gen_range(0..self.values.len());
        self.values[random_index]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */

fn main() {
    let mut randomized_set = RandomizedSet::new();

    // Insert values
    println!("{}", randomized_set.insert(1)); // true
    println!("{}", randomized_set.insert(2)); // true
    println!("{}", randomized_set.insert(2)); // false

    // Remove values
    println!("{}", randomized_set.remove(1)); // true
    println!("{}", randomized_set.remove(3)); // false

    // Get random value
    println!("{}", randomized_set.get_random()); // Randomly 2
}
