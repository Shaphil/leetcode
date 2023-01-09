/*
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

Runtime: 66 ms
Memory: 43.6 MB
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/874807873/
*/

function subtractProductAndSum(n: number): number {
  let s = n.toString().split('');
  let nums = s.map((x) => parseInt(x));
  let sum = nums.reduce((a, b) => a + b, 0);
  let prod = nums.reduce((a, b) => a * b, 1);

  return prod - sum;
}

function main() {
  let n = 4421;
  let result = subtractProductAndSum(n);
  console.log(result);
}

main();
