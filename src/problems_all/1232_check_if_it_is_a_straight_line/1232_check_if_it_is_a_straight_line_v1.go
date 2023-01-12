/*
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

Runtime: 2 ms
Memory: 3.5 MB
https://leetcode.com/problems/check-if-it-is-a-straight-line/submissions/876906045/
*/

package main

import "fmt"

func main() {
	coordinates := [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}}
	result := checkStraightLine(coordinates)
	fmt.Println(result)
}

func checkStraightLine(coordinates [][]int) bool {
	isStraight := true
	if len(coordinates) == 2 {
		return isStraight
	}

	x1 := coordinates[0][0]
	y1 := coordinates[0][1]
	x2 := coordinates[1][0]
	y2 := coordinates[1][1]

	var slope float64
	if x2-x1 == 0 {
		slope = float64(x1)
	} else {
		slope = float64(y2-y1) / float64(x2-x1)
	}

	for i := 1; i < len(coordinates)-1; i++ {
		x1 = coordinates[i][0]
		y1 = coordinates[i][1]
		x2 = coordinates[i+1][0]
		y2 = coordinates[i+1][1]

		var newSlope float64
		if x2-x1 == 0 {
			newSlope = float64(x1)
		} else {
			newSlope = float64(y2-y1) / float64(x2-x1)
		}

		if newSlope != slope {
			isStraight = false
			break
		}
	}

	return isStraight
}
