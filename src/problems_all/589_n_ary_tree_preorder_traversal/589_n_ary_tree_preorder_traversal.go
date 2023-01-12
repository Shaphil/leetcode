/*
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Runtime: 4 ms
Memory: 4 MB
https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/876786343/
*/

package main

import "fmt"

type Node struct {
	Val      int
	Children []*Node
}

func preorder(root *Node) []int {
	var pre []int
	preorderRecursive(root, &pre)
	return pre
}

func preorderRecursive(root *Node, pre *[]int) {
	if root != nil {
		*pre = append(*pre, root.Val)
		if root.Children != nil {
			for _, child := range root.Children {
				preorderRecursive(child, pre)
			}
		}
	}
}

func main() {
	tree := Node{1, []*Node{
		{3, []*Node{
			{5, []*Node{}},
			{6, []*Node{}},
		}},
		{2, []*Node{}},
		{4, []*Node{}},
	}}

	// childrenLevel_1 := []*Node{&Node{3, []*Node{}}, &Node{2, []*Node{}}, &Node{4, []*Node{}}}
	// childrenLevel_2 := []*Node{&Node{5, []*Node{}}, &Node{6, []*Node{}}}
	// tree.Children = childrenLevel_1
	// tree.Children[0].Children = childrenLevel_2

	result := preorder(&tree)
	fmt.Println(result)
}
