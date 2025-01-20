/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.39 MB
Beats:              25.00%
Submission:         https://leetcode.com/problems/cousins-in-binary-tree/submissions/1514718150/
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
    pub fn is_cousins(root: Option<Rc<RefCell<TreeNode>>>, x: i32, y: i32) -> bool {
        if root.is_none() {
            return false;
        }

        let mut queue = VecDeque::new();
        queue.push_back((root.clone(), None));

        while !queue.is_empty() {
            let level_size = queue.len();
            let mut x_parent = None;
            let mut y_parent = None;

            for _ in 0..level_size {
                let (current, parent) = queue.pop_front().unwrap();

                if let Some(node) = current {
                    let borrowed = node.borrow();
                    if borrowed.val == x {
                        x_parent = parent.clone();
                    }
                    if borrowed.val == y {
                        y_parent = parent.clone();
                    }

                    if let Some(left) = &borrowed.left {
                        queue.push_back((Some(left.clone()), Some(node.clone())));
                    }
                    if let Some(right) = &borrowed.right {
                        queue.push_back((Some(right.clone()), Some(node.clone())));
                    }
                }
            }

            if x_parent.is_some() && y_parent.is_some() {
                return x_parent != y_parent;
            }
            if x_parent.is_some() || y_parent.is_some() {
                return false;
            }
        }

        false
    }
}

fn main() {
    let root = create_tree(&[Some(1), Some(2), Some(3), None, Some(4), None, Some(5)]);
    let x = 4;
    let y = 5;
    let result = Solution::is_cousins(root, x, y);
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
