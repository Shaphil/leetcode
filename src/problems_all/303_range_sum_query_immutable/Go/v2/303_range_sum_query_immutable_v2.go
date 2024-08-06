/*
https://leetcode.com/problems/range-sum-query-immutable/description/

Runtime: 90 ms
Memory: 9.5 MB
https://leetcode.com/problems/range-sum-query-immutable/submissions/881291377/
*/

package main

import "fmt"

type NumArray struct {
	prefixSum []int
}

func Constructor(nums []int) NumArray {
	prefixSum := make([]int, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		prefixSum[i+1] = prefixSum[i] + nums[i]
	}

	return NumArray{prefixSum: prefixSum}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.prefixSum[right+1] - this.prefixSum[left]
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	arr := Constructor(nums)

	res := arr.SumRange(0, 4)
	fmt.Println(res)
}
