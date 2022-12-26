/*
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

Runtime: 0 ms
Memory: 1.9 MB
*/

package main

import "fmt"

func main() {
	n := 4421
	result := subtractProductAndSum(n)
	fmt.Println(result)
}

func subtractProductAndSum(n int) int {
	total := 0
	product := 1

	for n > 0 {
		i := n % 10
		total += i
		product *= i
		n /= 10
	}

	result := product - total
	return result
}
