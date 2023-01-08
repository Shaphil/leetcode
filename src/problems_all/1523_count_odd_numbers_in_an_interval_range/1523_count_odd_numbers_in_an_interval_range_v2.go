/*
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

O(n)
Runtime: 2519 ms
Memory: 1.8 MB
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/873928584/
*/

package main

import "fmt"

func main() {
	low := 1
	high := 11
	result := countOdds(low, high)
	fmt.Println(result)
}

func countOdds(low int, high int) int {
	count := 0
	for i := low; i <= high; i++ {
		if i%2 == 1 {
			count++
		}
	}
	return count
}
