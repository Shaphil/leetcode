/*
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


Runtime: 0 ms
Memory: 1.9 MB
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/880728604/
*/

package main

import (
	"fmt"
	"strconv"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	head := ListNode{1, &ListNode{0, &ListNode{1, nil}}}
	result := getDecimalValue(&head)
	fmt.Println(result)
}

func getDecimalValue(head *ListNode) int {
	binary := ""
	current := head
	for current != nil {
		binary += strconv.Itoa(current.Val)
		current = current.Next
	}

	val, err := strconv.ParseInt(binary, 2, 32)
	if err != nil {
		fmt.Println(err)
	}

	return int(val)
}
