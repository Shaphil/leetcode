/*
https://leetcode.com/problems/contains-duplicate/description/

Runtime: 105 ms
Memory: 9.6 MB
https://leetcode.com/problems/contains-duplicate/submissions/881242084/
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
