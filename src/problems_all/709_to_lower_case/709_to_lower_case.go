/*
https://leetcode.com/problems/to-lower-case/description/

Runtime: 0 ms
Memory: 2 MB
https://leetcode.com/problems/to-lower-case/submissions/879278971/
*/

package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "Hello"
	result := toLowerCase(s)
	fmt.Println(result)
}

func toLowerCase(s string) string {
	return strings.ToLower(s)
}
