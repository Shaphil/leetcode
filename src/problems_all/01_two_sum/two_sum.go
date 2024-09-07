/*
Runtime:    6 ms
Memory:     4.31 MB
Submission: https://leetcode.com/problems/two-sum/submissions/1382186205/
*/

package main

import "fmt"

func main() {
    target := 9
    nums := []int{2, 7, 11, 15}
    result := twoSum(nums, target)
    fmt.Println(result)
}

func twoSum(nums []int, target int) []int {
    numsToIndex := make(map[int]int)

    for i, num := range nums {
        complement := target - num

        if _, ok := numsToIndex[complement]; ok {
            return []int{numsToIndex[complement], i}
        }
        numsToIndex[num] = i
    }

    return []int{}
}