/*
Runtime:            4 ms
Beats:              25.00%
Memory:             10.16 MB
Beats:              0%
Submission:         https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/1499634987/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #linked-list, #two-pointers
Solved By:          #linked-list
*/

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

struct Solution {}

impl Solution {
    pub fn swap_nodes(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut nodes = Vec::new();
        let mut current = head.as_mut();

        // Step 1: Populate the vector with raw pointers to the nodes
        while let Some(node) = current {
            nodes.push(&mut **node as *mut ListNode); // Dereference Box and store raw pointer
            current = node.next.as_mut();
        }

        // Step 2: Swap the values of the k-th node from the start and end
        let len = nodes.len();
        unsafe {
            let temp = (*nodes[k as usize - 1]).val;
            (*nodes[k as usize - 1]).val = (*nodes[len - k as usize]).val;
            (*nodes[len - k as usize]).val = temp;
        }

        head // Return the modified linked list
    }
}

fn main() {
    let list = vec![1, 2, 3, 4, 5];
    let k = 2;

    let mut head = None;
    let mut current = &mut head;

    for &val in list.iter() {
        let node = Some(Box::new(ListNode::new(val)));
        *current = node;
        current = &mut current.as_mut().unwrap().next;
    }

    let result = Solution::swap_nodes(head, k);
    print_list(result);
}

fn print_list(head: Option<Box<ListNode>>) {
    let mut current = head.as_ref();
    let mut list = Vec::new();
    while let Some(node) = current {
        list.push(node.val);
        current = node.next.as_ref();
    }
    println!("{:?}", list);
}
