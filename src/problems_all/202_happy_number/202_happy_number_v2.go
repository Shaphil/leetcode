/*
https://leetcode.com/problems/happy-number/description/

Runtime: 0 ms
Memory: 2 MB
https://leetcode.com/problems/happy-number/submissions/881273371/
*/

package main

import "fmt"

func main() {
	n := 7
	result := isHappy(n)
	fmt.Println(result)
}

func sumOfDigits(n int) int {
	total := 0
	for n > 0 {
		digit := n % 10
		total += (digit * digit)
		n /= 10
	}
	return total
}

func isHappy(n int) bool {
	if n == 1 {
		return true
	}

	happy := true
	seq := map[int]bool{}
	for {
		total := sumOfDigits(n)

		if total == 1 {
			break
		}

		if _, ok := seq[total]; ok {
			happy = false
			break
		}

		seq[total] = true
		n = total
	}

	return happy
}
