/*
Runtime:            12 ms
Beats:              82.19%
Memory:             10.66 MB
Beats:              61.25%
Submission:         https://leetcode.com/problems/contains-duplicate/submissions/1484718403/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sorting
Solved By:          #hash-table
*/

package main

import (
	"fmt"
)

func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)
	for _, num := range nums {
		if seen[num] {
			return true
		}
		seen[num] = true
	}

	return false

}

func main() {
	nums := []int{1, 2, 3, 4}
	result := containsDuplicate(nums)
	fmt.Println(result)
}
