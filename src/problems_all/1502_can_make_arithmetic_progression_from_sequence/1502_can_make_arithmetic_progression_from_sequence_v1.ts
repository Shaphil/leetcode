/*
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Runtime: 74 ms
Memory: 44.6 MB
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/876117048/
*/

function canMakeArithmeticProgression(arr: number[]): boolean {
  arr.sort((a, b) => a - b);

  let isProg = true;
  let diff = arr[1] - arr[0];

  for (let i = 2; i < arr.length; i++) {
    let _diff = arr[i] - arr[i - 1];
    if (_diff != diff) {
      isProg = false;
      break;
    }
  }

  return isProg;
}

function main() {
  let arr = [3, 5, 1];
  const result = canMakeArithmeticProgression(arr);
  console.log(result);
}

main();
