/*
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

Runtime: 108 ms
Memory: 7.3 MB
Submission - https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/submissions/866388201/
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	x, y := 3, 4
	points := [][]int{{1, 2}, {3, 1}, {2, 4}, {2, 3}, {4, 4}}
	result := nearestValidPoint(x, y, points)
	fmt.Println(result)
}

func nearestValidPoint(x int, y int, points [][]int) int {
	closest := math.Inf(1)
	closestIdx := -1

	for i, point := range points {
		_x, _y := point[0], point[1]
		if x == _x || y == _y {
			dist := math.Abs(float64(x-_x)) + math.Abs(float64(y-_y))
			if dist < closest {
				closest = dist
				closestIdx = i
			}
		}
	}

	return closestIdx
}
