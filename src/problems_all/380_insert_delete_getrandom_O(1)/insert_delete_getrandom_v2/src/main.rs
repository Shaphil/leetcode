/*
Runtime:            32 ms
Beats:              83.33%
Memory:             30.07 MB
Beats:              5.05%
Submission:         https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1475431475/
Time complexity:    Insert: O(1), O(n) worst case; Remove: O(1), O(n) worst case; getRandom: O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #math, #design, #randomized
Solved By:          #hash-table
*/

use rand::Rng;
use std::collections::{HashMap, HashSet};

struct RandomizedSet {
    nums: Vec<i32>,
    index_map: HashMap<i32, usize>,
    set: HashSet<i32>,
}

impl RandomizedSet {
    fn new() -> Self {
        Self {
            nums: Vec::new(),
            index_map: HashMap::new(),
            set: HashSet::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if self.set.contains(&val) {
            return false;
        }

        self.set.insert(val);
        self.nums.push(val);
        self.index_map.insert(val, self.nums.len() - 1);
        true
    }

    fn remove(&mut self, val: i32) -> bool {
        if !self.set.contains(&val) {
            return false;
        }

        self.set.remove(&val);
        let last_val = self.nums.pop().unwrap();
        let val_index = self.index_map.remove(&val).unwrap();

        if last_val != val {
            self.nums[val_index] = last_val;
            self.index_map.insert(last_val, val_index);
        }

        true
    }

    fn get_random(&self) -> i32 {
        let random_index = rand::thread_rng().gen_range(0..self.nums.len());
        self.nums[random_index]
    }
}

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
