/*
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 71 ms
Memory: 45.5 MB
https://leetcode.com/problems/number-of-1-bits/submissions/874794129/
*/

function toBinary(n: number): string {
  let bin = '';
  while (n > 0) {
    let r = n % 2;
    bin += r;

    // manual integer division
    let x = n / 2; // x = (15 / 2) = 7.5
    x = x * 10; // x = 7.5 * 10 = 75
    n = (x - (x % 10)) / 10; // n = (75 - (75 % 10)) / 10 = (75 - 5) / 10 = 7
  }

  return bin;
}

function hammingWeight(n: number): number {
  // let bin = (n >>> 0).toString(2);
  let bin = toBinary(n);
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
