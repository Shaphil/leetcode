/*
https://leetcode.com/problems/next-greater-element-i/


Runtime: 90 ms
Memory: 46.2 MB

https://leetcode.com/problems/next-greater-element-i/submissions/876878660/
*/

function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
  let n2items: { [key: number]: number } = {};
  for (let [i, v] of nums2.entries()) {
    n2items[v] = i;
  }

  let result: number[] = [];
  for (let i of nums1) {
    const idx = n2items[i];
    let nextBig = -Infinity;

    for (let j = idx + 1; j < nums2.length; j++) {
      if (nums2[j] > nextBig && nums2[j] > i) {
        nextBig = nums2[j];
        break;
      }
    }

    if (nextBig == -Infinity) {
      result.push(-1);
    } else {
      result.push(nextBig);
    }
  }

  return result;
}

function main() {
  let nums1 = [4, 1, 2];
  let nums2 = [1, 3, 4, 2];
  let result = nextGreaterElement(nums1, nums2);
  console.log(result);
}

main();
