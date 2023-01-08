/*
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

O(n)
Runtime: 0 ms
Memory: 1.9 MB
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/submissions/874163609/
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	salary := []int{48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000, 37000, 93000, 77000, 33000, 28000, 4000, 54000, 67000, 6000, 1000, 11000}
	result := average(salary)
	fmt.Println(result)
}

func minMaxSum(arr []int) (int, int, int) {
	min := math.MaxInt64
	max := math.MinInt64
	sum := 0

	for _, i := range arr {
		if i > max {
			max = i
		}

		if i < min {
			min = i
		}

		sum += i
	}

	return min, max, sum
}

func average(salary []int) float64 {
	min, max, sum := minMaxSum(salary)
	avg := float64(sum-min-max) / float64(len(salary)-2)

	return avg
}
