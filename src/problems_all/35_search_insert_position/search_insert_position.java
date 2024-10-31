/*
Runtime:    0 ms
Beats:      100.00%
Memory:     42.81 MB
Beats:      53.16%
Submission: https://leetcode.com/problems/search-insert-position/submissions/1439205025/
*/

class Solution {
    private int binarySearch(int[] arr, int lo, int hi, int x) {
        if (hi >= lo) {
            int mid = (hi + lo) / 2;

            if (mid >= arr.length) {
                return -1;
            }

            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] > x) {
                return binarySearch(arr, lo, mid - 1, x);
            } else {
                return binarySearch(arr, mid + 1, hi, x);
            }
        } else {
            return -1;
        }
    }

    public int searchInsert(int[] nums, int target) {
        int res = binarySearch(nums, 0, nums.length, target);
        if (res != -1) {
            return res;
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] > target) {
                    return i;
                }
            }

            return nums.length;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 3, 5, 6};
        int target = 7;

        Solution solution = new Solution();
        int result = solution.searchInsert(nums, target);
        System.out.println(result);
    }
}