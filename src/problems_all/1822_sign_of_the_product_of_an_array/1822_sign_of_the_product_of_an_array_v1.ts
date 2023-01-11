/*
https://leetcode.com/problems/sign-of-the-product-of-an-array/

Runtime: 71 ms
Memory: 44.7 MB
https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/876104315/
*/

function signFunc(x: number): number {
  if (x > 0) return 1;
  else if (x < 0) return -1;
  else return 0;
}

function arraySign(nums: number[]): number {
  let prod = nums.reduce((a, b) => a * b, 1);
  return signFunc(prod);
}

function main() {
  let nums = [9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24];
  let result = arraySign(nums);
  console.log(result);
}

main();
