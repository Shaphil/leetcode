/*
Runtime:            4 ms
Beats:				48.67%
Memory:             6.07 MB
Beats:              66.59%
Submission:         https://leetcode.com/problems/palindrome-number/submissions/1998212217/
Time complexity:    O(log10 n)
Space complexity:   O(1)
Topics:             #math
Solved By:          #math
*/

package main

import (
	"fmt"
)

func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	rev := 0
	for x > rev {
		digit := x % 10
		rev = rev*10 + digit
		x /= 10
	}
	return x == rev || x == rev/10
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(10))
}
