/*
Runtime:    0 ms
Beats:	    100.00%
Memory: 	2.89 MB
Beats:	    5.81%
Submission:	https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1468503469/
Topics:     #array, #divide-and-conquer, #tree, #binary-search-tree, #binary-tree
Solved By:  #divide-and-conquer, #recursion
*/

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

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

struct Solution {}

impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.is_empty() {
            return None;
        }

        let mid = nums.len() / 2;
        let root = Rc::new(RefCell::new(TreeNode::new(nums[mid])));
        root.borrow_mut().left = Self::sorted_array_to_bst(nums[..mid].to_vec());
        root.borrow_mut().right = Self::sorted_array_to_bst(nums[mid + 1..].to_vec());

        Some(root)
    }
}

fn print_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
    let mut result = Vec::new();
    let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
    queue.push_back(root);

    while !queue.is_empty() {
        let level_size = queue.len();
        for _ in 0..level_size {
            let node = queue.pop_front().unwrap();
            if let Some(node) = node {
                result.push(node.borrow().val.to_string());
                queue.push_back(Option::from(node.borrow().left.clone()));
                queue.push_back(Option::from(node.borrow().right.clone()));
            } else {
                result.push("null".to_string());
            }
        }
    }

    result
}

fn main() {
    let nums = Vec::from([-10, -3, 0, 5, 9]);
    let result = Solution::sorted_array_to_bst(nums);
    let res = print_tree(result);
    println!("{:?}", res);
}
