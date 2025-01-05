/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.20 MB
Beats:              66.67%
Submission:         https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1498660491/
Time complexity:    O(L), where `L` is the length of the list
Space complexity:   O(1)
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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode { val: 0, next: head }));
        let mut length = 0;

        {
            // First pass: Calculate the length of the list
            let mut current = dummy.as_ref();
            while let Some(node) = current {
                length += 1;
                current = node.next.as_ref();
            }
        }

        length -= 1; // Adjust length to ignore the dummy node

        // Second pass: Traverse to the (length - n)th node
        let mut current = dummy.as_mut();
        for _ in 0..(length - n) {
            current = current.unwrap().next.as_mut();
        }

        // Remove the nth node
        let next = current.as_mut().unwrap().next.as_mut().unwrap().next.take();
        current.as_mut().unwrap().next = next;

        dummy.unwrap().next
    }
}

fn main() {
    let head = create_linked_list(vec![1, 2, 3, 4, 5]);
    let n = 2;
    let result = Solution::remove_nth_from_end(head, n);
    print_list(result);
}

// Helper function to create a linked list from a vector
fn create_linked_list(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut head = None;
    let mut tail = &mut head;

    for &val in &values {
        let new_node = Some(Box::new(ListNode::new(val)));
        *tail = new_node;
        tail = &mut tail.as_mut().unwrap().next;
    }

    head
}

// Helper function to print the linked list
fn print_list(head: Option<Box<ListNode>>) {
    let mut current = head.as_ref();
    let mut list = Vec::new();
    while let Some(node) = current {
        list.insert(0, node.val);
        current = node.next.as_ref();
    }
    list.reverse();
    println!("{:?}", list);
}
