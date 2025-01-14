/*
Runtime:            6 ms
Beats:              75.00%
Memory:             13.05 MB
Beats:              56.25%
Submission:         https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/1508758456/
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
use std::collections::VecDeque;
use std::rc::Rc;

struct Solution {}

impl Solution {
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }

        let mut queue = VecDeque::new();
        queue.push_back((root.unwrap(), 1));

        while let Some((node, depth)) = queue.pop_front() {
            let left = node.borrow().left.clone();
            let right = node.borrow().right.clone();

            // Check if it's a leaf node
            if left.is_none() && right.is_none() {
                return depth;
            }

            if let Some(left_child) = left {
                queue.push_back((left_child, depth + 1));
            }

            if let Some(right_child) = right {
                queue.push_back((right_child, depth + 1));
            }
        }

        0
    }
}

fn main() {
    let root = create_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)]);
    let result = Solution::min_depth(root);
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
