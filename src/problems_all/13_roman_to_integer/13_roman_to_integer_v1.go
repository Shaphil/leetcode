/*
Runtime:	4 ms
RT Beats:	69.52%
Memory: 	2.95 MB
Mem Beats:	81.21%
Submission:	https://leetcode.com/problems/roman-to-integer/submissions/1421110008/
*/

package main

import "fmt"

var ROMAN_TO_INT = map[rune]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

func romanToInt(s string) int {
	total := 0
	prev := 0

	for _, c := range s {
		current := ROMAN_TO_INT[c]
		if current > prev {
			total += current - 2*prev
		} else {
			total += current
		}

		prev = current
	}

	return total
}

func main() {
	s := "MCMXCIV"
	result := romanToInt(s)
	fmt.Println(result)
}
