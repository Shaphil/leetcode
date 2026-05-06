/*
Runtime:            3 ms
Beats:				57.03%
Memory:             6.18 MB
Beats:              44.63%
Submission:         https://leetcode.com/problems/palindrome-number/submissions/1996871011/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
*/

package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	s := strconv.Itoa(x)
	runes := []rune(s)

	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	inv := string(runes)
	return inv == s
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(10))
}
