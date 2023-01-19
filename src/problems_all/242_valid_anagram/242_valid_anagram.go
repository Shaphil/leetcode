/*
https://leetcode.com/problems/valid-anagram/description/

Runtime: 20 ms
Memory: 2.8 MB
https://leetcode.com/problems/valid-anagram/submissions/881234609/
*/

package main

import (
	"fmt"
	"reflect"
)

func main() {
	s := "anagram"
	t := "nagaram"
	result := isAnagram(s, t)
	fmt.Println(result)
}

func Counter(s string) map[string]int {
	counter := map[string]int{}
	for _, char := range s {
		ch := fmt.Sprintf("%c", char)
		if count, ok := counter[ch]; ok {
			counter[ch] = count + 1
		} else {
			counter[ch] = 1
		}
	}
	return counter
}

func isAnagram(s string, t string) bool {
	return reflect.DeepEqual(Counter(s), Counter(t))
}
