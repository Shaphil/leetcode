/*
Runtime:            4 ms
Beats:              87.50%
Memory:             13.58 MB
Beats:              5.36%
Submission:         https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/1508752081/
Time complexity:    O(n)
Space complexity:   O(h) avg, where `h` = tree height, O(n) worst
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #dfs
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
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }

        let node = root.unwrap();
        let left = node.borrow().left.clone();
        let right = node.borrow().right.clone();

        if left.is_none() {
            return 1 + Solution::min_depth(right);
        }

        if right.is_none() {
            return 1 + Solution::min_depth(left);
        }

        1 + std::cmp::min(Solution::min_depth(left), Solution::min_depth(right))
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
