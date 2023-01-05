/*
https://leetcode.com/problems/next-greater-element-i/


Runtime: 0 ms
Memory: 3.6 MB

https://leetcode.com/problems/next-greater-element-i/submissions/871877680/
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	nums1 := []int{4, 1, 2}
	nums2 := []int{1, 3, 4, 2}
	result := nextGreaterElement(nums1, nums2)
	fmt.Println(result)
}

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	n2items := map[int]int{}
	for i, v := range nums2 {
		n2items[v] = i
	}

	result := []int{}
	for _, i := range nums1 {
		idx := n2items[i]
		nextBig := math.Inf(1)

		for j := idx; j < len(nums2); j++ {
			if nums2[j] > int(nextBig) && nums2[j] > i {
				nextBig = float64(nums2[j])
				break
			}
		}

		if nextBig == math.Inf(1) {
			result = append(result, -1)
		} else {
			result = append(result, int(nextBig))
		}
	}

	return result
}
