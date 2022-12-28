/*
https://leetcode.com/problems/sign-of-the-product-of-an-array/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/sign-of-the-product-of-an-array/

Runtime: 6 ms
Memory: 3.2 MB
https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/866994256/
*/

package main

import "fmt"

func main() {
	nums := []int{9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24}
	result := arraySign(nums)
	fmt.Println(result)
}

func arraySign(nums []int) int {
	var prod float64 = 1
	for _, i := range nums {
		prod *= float64(i)
	}
	return signFunc(prod)
}

func signFunc(x float64) int {
	if x > 0 {
		return 1
	} else if x < 0 {
		return -1
	} else {
		return 0
	}
}
