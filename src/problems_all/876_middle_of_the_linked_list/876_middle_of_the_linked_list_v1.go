/*
https://leetcode.com/problems/middle-of-the-linked-list/


Runtime: 0 ms
Memory: 1.9 MB
https://leetcode.com/problems/middle-of-the-linked-list/submissions/880716823/
*/

package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	list := ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, &ListNode{6, nil}}}}}}
	result := middleNode(&list)
	printList(result)
}

func middleNode(head *ListNode) *ListNode {
	length := 0
	current := head
	for current != nil {
		current = current.Next
		length++
	}

	length = length / 2
	current = head
	for ; length > 0; length-- {
		current = current.Next
	}

	return current
}

func printList(head *ListNode) {
	current := head
	for current != nil {
		fmt.Printf("%d ", current.Val)
		current = current.Next
	}
}

// class Solution:
//     def middleNode(self, head: ListNode) -> ListNode:
//         length = 0
//         current = head
//         while current:
//             current = current.next
//             length += 1

//         length = length // 2
//         current = head
//         while length > 0:
//             current = current.next
//             length -= 1

//         return current
