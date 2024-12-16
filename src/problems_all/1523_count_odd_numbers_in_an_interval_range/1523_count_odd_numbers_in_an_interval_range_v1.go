/*

Runtime:            0 ms
Memory:             1.9 MB
Submission:         https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/873924721/
Time complexity:    O(1)
Space complexity:   O(1)
Topics:             #math
Solved By:          #math
*/

package main

import "fmt"

func main() {
	low := 1
	high := 11
	result := countOdds(low, high)
	fmt.Println(result)
}

func If(cond bool, truthy, falsy int) int {
	if cond {
		return truthy
	}
	return falsy
}

func countOdds(low int, high int) int {
	hi := If(high%2 == 0, high/2, (high+1)/2)
	lo := If(low%2 == 0, low/2, (low-1)/2)

	return hi - lo
}
