/*
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 0 ms
Memory: 1.8 MB
*/

package main

import (
	"fmt"
	"strings"
)

func main() {
	var n uint32 = 2147483647
	result := hammingWeight(n)
	fmt.Println(result)
}

func hammingWeight(num uint32) int {
	bin := fmt.Sprintf("%b", num)
	ones := strings.Count(bin, "1")

	return ones
}
