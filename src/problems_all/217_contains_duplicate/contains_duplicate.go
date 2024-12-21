/*
Runtime:            105 ms
Beats:              5.39%
Memory:             9.6 MB
Beats:              96.17%
Submission:         https://leetcode.com/problems/contains-duplicate/submissions/881242084/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sorting
Solved By:          #hash-table
*/

package main

import "fmt"

func main() {
	nums := []int{1, 2, 3, 4}
	result := containsDuplicate(nums)
	fmt.Println(result)
}

func containsDuplicate(nums []int) bool {
	counter := map[int]int8{}
	for _, num := range nums {
		if _, ok := counter[num]; ok {
			return true
		} else {
			counter[num] = 1
		}
	}

	return false
}
