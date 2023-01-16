/*
https://leetcode.com/problems/move-zeroes/description/

O(n)
Runtime: 22 ms
Memory: 6.6 MB
*/

package main

import "fmt"

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeroes(nums)
	fmt.Println(nums)
}

func moveZeroes(nums []int) {
	// fill in the zeroes with non-zero values
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[count] = nums[i]
			count++
		}
	}

	// Now all the non-zero values are at the beginning.
	// Fill the `len(nums) - count` items at the end with zeroes.
	for count < len(nums) {
		nums[count] = 0
		count++
	}
}
