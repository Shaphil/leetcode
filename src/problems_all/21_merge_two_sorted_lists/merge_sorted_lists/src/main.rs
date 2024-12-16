/*
Runtime:            0 ms
Beats:              100.00%
Memory:             2.19 MB
Beats:              43.29%
Submission:         https://leetcode.com/problems/merge-two-sorted-lists/submissions/1480367112/
Time complexity:    O(n + m)
Space complexity:   O(1)
Topics:             #linked-list, #recursion
Solved By:          #linked-list
*/

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution {}

impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Create a dummy node for convenience
        let mut dummy = ListNode::new(0);
        let mut current = &mut dummy;

        let mut l1 = list1;
        let mut l2 = list2;

        // Iterate through both lists and compare values
        while l1.is_some() && l2.is_some() {
            let val1 = l1.as_ref().unwrap().val;
            let val2 = l2.as_ref().unwrap().val;

            if val1 <= val2 {
                current.next = Some(Box::new(ListNode::new(val1)));
                l1 = l1.unwrap().next;
            } else {
                current.next = Some(Box::new(ListNode::new(val2)));
                l2 = l2.unwrap().next;
            }
            current = current.next.as_mut().unwrap();
        }

        // Append remaining elements from the non-empty list
        current.next = l1.or(l2);

        // Return the merged list (excluding the dummy node)
        dummy.next
    }
}

fn main() {
    // Create linked lists
    let mut list1 = Some(Box::new(ListNode::new(1)));
    list1.as_mut().unwrap().next = Some(Box::new(ListNode::new(2)));
    list1.as_mut().unwrap().next.as_mut().unwrap().next = Some(Box::new(ListNode::new(4)));

    let mut list2 = Some(Box::new(ListNode::new(1)));
    list2.as_mut().unwrap().next = Some(Box::new(ListNode::new(3)));
    list2.as_mut().unwrap().next.as_mut().unwrap().next = Some(Box::new(ListNode::new(4)));

    // Merge the lists
    let merged_list = Solution::merge_two_lists(list1, list2);

    // Print the merged list
    let mut current = merged_list;
    while current.is_some() {
        print!("{} ", current.as_ref().unwrap().val);
        current = current.unwrap().next;
    }
    println!();
}
