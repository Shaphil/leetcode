/*
https://leetcode.com/problems/range-sum-query-immutable/description/

Runtime: 90 ms
Memory: 9.5 MB
https://leetcode.com/problems/range-sum-query-immutable/submissions/881291377/
*/

package main

import "fmt"

type NumArray struct {
	nums []int
}

func Constructor(nums []int) NumArray {
	arr := NumArray{nums: nums}
	return arr
}

func (this *NumArray) SumRange(left int, right int) int {
	total := 0
	for i := left; i < right+1; i++ {
		total += this.nums[i]
	}

	return total
}

func main() {
	nums := []int{-2, 0, 3, -5, 2, -1}
	arr := Constructor(nums)

	res := arr.SumRange(0, 2)
	fmt.Println(res)

	res = arr.SumRange(2, 5)
	fmt.Println(res)

	res = arr.SumRange(0, 5)
	fmt.Println(res)
}
