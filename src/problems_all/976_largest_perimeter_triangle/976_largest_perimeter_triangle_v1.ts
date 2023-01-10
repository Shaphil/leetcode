/*
https://leetcode.com/problems/largest-perimeter-triangle/

Runtime: 120 ms
Memory: 46.8 MB
https://leetcode.com/problems/largest-perimeter-triangle/submissions/875605541/
*/

function largestPerimeter(nums: number[]): number {
  let perimeter = 0;
  nums.sort((a, b) => b - a);

  for (let i = 0; i < nums.length - 2; i++) {
    let [a, b, c] = nums.slice(i, i + 3);
    if (b + c > a) {
      perimeter = a + b + c;
      break;
    }
  }

  return perimeter;
}

function main() {
  let nums = [3, 6, 2, 3];
  let result = largestPerimeter(nums);
  console.log(result);
}

main();
