/*
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Runtime: 4 ms
Memory: 2.4 MB
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/867006444/
*/

package main

import (
	"fmt"
	"sort"
)

func main() {
	arr := []int{3, 5, 1}
	result := canMakeArithmeticProgression(arr)
	fmt.Println(result)
}

func canMakeArithmeticProgression(arr []int) bool {
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})
	diff := arr[1] - arr[0]
	is_prog := true
	for i := 1; i < len(arr); i++ {
		_diff := arr[i] - arr[i-1]
		if _diff != diff {
			is_prog = false
			break
		}
	}

	return is_prog
}
