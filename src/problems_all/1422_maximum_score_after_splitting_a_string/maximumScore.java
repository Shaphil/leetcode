/*
Runtime:            1 ms
Beats:              97.41%
Memory:             41.66 MB
Beats:              36.37%
Submission:         https://leetcode.com/problems/maximum-score-after-splitting-a-string/submissions/1495444809/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #string, #prefix-sum
Solved By:          #prefix-sum
*/

class Solution {
    public int maxScore(String s) {
        int totalOnes = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') {
                totalOnes++;
            }
        }

        int maxScore = 0;
        int zerosLeft = 0;
        int onesRight = totalOnes;

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0') {
                zerosLeft++;
            } else {
                onesRight--;
            }

            maxScore = Math.max(maxScore, zerosLeft + onesRight);
        }

        return maxScore;
    }

    public static void main(String[] args) {
        String s = "011101";
        var result = new Solution().maxScore(s);
        System.out.println(result);
    }
}