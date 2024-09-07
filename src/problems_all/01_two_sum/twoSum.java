/*
Runtime:    2 ms
Memory:     45.03 MB
Submission: https://leetcode.com/problems/two-sum/submissions/1382250169/
*/

import java.util.HashMap;
import java.util.Arrays;

public class Main {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();
        int[] res = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numToIndex.containsKey(complement)) {
                res[0] = numToIndex.get(complement);
                res[1] = i;
                return res;
            }
            numToIndex.put(nums[i], i);
        }

        return new int[0];
    }

    public static void main(String[] args) {
        int target = 9;
        int[] nums = {2, 7, 11, 15};

        int[] result = twoSum(nums, target);

        System.out.println(Arrays.toString(result));
    }
}