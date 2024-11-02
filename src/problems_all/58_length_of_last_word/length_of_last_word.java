/*
Runtime:    0 ms
Beats:      100.00%
Memory:     41.80 MB
Beats:      33.76%
Submission: https://leetcode.com/problems/length-of-last-word/submissions/1440847575/
*/

class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        return words[words.length - 1].length();
    }

    public static void main(String[] args) {
        String s = "world";
        Solution solution = new Solution();
        int result = solution.lengthOfLastWord(s);
        System.out.println(result);
    }
}