/*
Runtime:            3 ms
Beats:              23.66%
Memory:             6.98 MB
Beats:              44.97%
Submission:         https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1999168135/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #binary-search, #divide-and-conquer
Solved By:          #array
*/

package main

import (
	"fmt"
	"sort"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	merged := append(nums1, nums2...)
	sort.Ints(merged)
	total := len(merged)

	if total%2 == 1 {
		return float64(merged[total/2])
	}

	mid1 := merged[total/2-1]
	mid2 := merged[total/2]
	return float64(mid1+mid2) / 2.0
}

func main() {
	nums1 := []int{1, 2}
	nums2 := []int{3, 4}
	result := findMedianSortedArrays(nums1, nums2)
	fmt.Println(result)
}
