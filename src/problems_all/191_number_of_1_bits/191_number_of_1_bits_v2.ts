/*
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 74 ms
Memory: 44.2 MB
https://leetcode.com/problems/number-of-1-bits/submissions/874795349/
*/


function hammingWeight(n: number): number {
  let bin = (n >>> 0).toString(2);
  let count = 0;
  for (let c of bin) {
    if (c === '1') {
      count++;
    }
  }

  return count;
}

function main(): void {
  let n = 2147483647;
  let result = hammingWeight(n);
  console.log(result);
}

main();
