/*
Runtime:            0 ms
Beats:              100.00%
Memory:             3.04 MB
Beats:              58.14%
Submission:         https://leetcode.com/problems/average-of-levels-in-binary-tree/submissions/1510591577/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #bfs
*/

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

struct Solution {}

impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut result = Vec::new();
        if root.is_none() {
            return result;
        }

        let mut queue = Vec::new();
        queue.push(root.clone());

        while !queue.is_empty() {
            let level_size = queue.len();
            let mut level: Vec<i64> = Vec::with_capacity(level_size);

            for _ in 0..level_size {
                let node = queue.remove(0).unwrap();
                level.push(node.borrow().val as i64);

                if let Some(left) = &node.borrow().left {
                    queue.push(Option::from(left.clone()));
                }
                if let Some(right) = &node.borrow().right {
                    queue.push(Option::from(right.clone()));
                };
            }
            let total: i64 = level.iter().sum();
            let avg = total as f64 / level.len() as f64;
            result.push(avg)
        }

        result
    }
}

fn main() {
    let root = create_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)]);
    let result = Solution::average_of_levels(root);
    println!("{:?}", result);
}

fn create_tree(values: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    if values.is_empty() {
        return None;
    }

    let nodes: Vec<Option<Rc<RefCell<TreeNode>>>> = values
        .iter()
        .map(|&val| match val {
            Some(v) => Some(Rc::new(RefCell::new(TreeNode::new(v)))),
            None => None,
        })
        .collect();

    for i in 0..nodes.len() / 2 {
        if let Some(node) = &nodes[i] {
            if 2 * i + 1 < nodes.len() && nodes[2 * i + 1].is_some() {
                node.borrow_mut().left = nodes[2 * i + 1].clone();
            }
            if 2 * i + 2 < nodes.len() && nodes[2 * i + 2].is_some() {
                node.borrow_mut().right = nodes[2 * i + 2].clone();
            }
        }
    }

    nodes[0].clone()
}
