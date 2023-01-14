/*
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Runtime: 9 ms
Memory: 7.7 MB
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/877522776/
*/

package main

import "fmt"

func main() {
	arr := []int{10, 11, 12}
	result := sumOddLengthSubarrays(arr)
	fmt.Println(result)
}

func sumOddLengthSubarrays(arr []int) int {
	oddNums := []int{}
	for i := 1; i < len(arr)+1; i += 2 {
		oddNums = append(oddNums, i)
	}

	oddArrayItems := []int{}
	for _, i := range oddNums {
		for j := 0; j < len(arr); j++ {
			if (i+j <= len(arr)) && (len(arr[j:j+i]) >= i) {
				oddArrayItems = append(oddArrayItems, arr[j:j+i]...)
			}
		}
	}

	return sum(oddArrayItems)
}

func sum(arr []int) int {
	total := 0
	for _, i := range arr {
		total += i
	}
	return total
}
