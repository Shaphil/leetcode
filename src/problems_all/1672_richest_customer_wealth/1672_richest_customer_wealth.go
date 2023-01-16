/*
https://leetcode.com/problems/richest-customer-wealth/

Runtime: 5 ms
Memory: 3 MB
https://leetcode.com/problems/richest-customer-wealth/submissions/879086931/
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	accounts := [][]int{{1, 2, 3}, {3, 2, 1}}
	result := maximumWealth(accounts)
	fmt.Println(result)
}

func sum(arr []int) int {
	total := 0
	for _, i := range arr {
		total += i
	}
	return total
}

func maximumWealth(accounts [][]int) int {
	maxWealth := int(math.Inf(-1))
	for _, account := range accounts {
		total := sum(account)
		if total > maxWealth {
			maxWealth = total
		}
	}
	return maxWealth
}
