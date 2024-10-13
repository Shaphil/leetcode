/*
Runtime:    3 ms
RTBeats:    83.54%
Memory:     44.76 MB
MemBeats:   38.48%
Submission: https://leetcode.com/problems/roman-to-integer/submissions/1421346714/
*/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final Map<Character, Integer> ROMAN_TO_INT = createMap();

    private static Map<Character, Integer> createMap() {
        Map<Character, Integer> romanToInt = new HashMap<>();

        romanToInt.put('I', 1);
        romanToInt.put('V', 5);
        romanToInt.put('X', 10);
        romanToInt.put('L', 50);
        romanToInt.put('C', 100);
        romanToInt.put('D', 500);
        romanToInt.put('M', 1000);

        return romanToInt;
    }

    public static Map<Character, Integer> getRomanToIntMap() {
        return ROMAN_TO_INT;
    }

    public static int romanToInt(String s) {
        int total = 0;
        int prev = 0;
        Map<Character, Integer> map = getRomanToIntMap();

        for (char c : s.toCharArray()) {
            int current = map.get(c);
            if (current > prev) {
                total += current - 2 * prev;
            } else {
                total += current;
            }

            prev = current;
        }

        return total;
    }

    public static void main(String[] args) {
        String s = "MCMXCIV";
        int result = romanToInt(s);
        System.out.println(result);
    }
}