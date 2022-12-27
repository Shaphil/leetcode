/*
https://leetcode.com/problems/largest-perimeter-triangle/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/largest-perimeter-triangle/

Runtime: 40 ms
Memory: 6.6 MB
*/

package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{1, 2, 1, 10}
	perimeter := largestPerimeter(nums)
	fmt.Println(perimeter)
}

func largestPerimeter(nums []int) int {
	perimeter := 0
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	for i := 0; i < len(nums)-2; i++ {
		a, b, c := nums[i], nums[i+1], nums[i+2]

		cond1 := a+b > c
		cond2 := a+c > b
		cond3 := b+c > a
		if cond1 && cond2 && cond3 {
			if a+b+c > perimeter {
				perimeter = a + b + c
				break
			}
		}
	}

	return perimeter
}
