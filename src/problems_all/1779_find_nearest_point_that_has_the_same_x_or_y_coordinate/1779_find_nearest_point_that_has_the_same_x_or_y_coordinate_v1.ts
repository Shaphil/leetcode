/*
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

Runtime: 91 ms
Memory: 50.9 MB
*/

function nearestValidPoint(x: number, y: number, points: number[][]): number {
  let closest = Infinity;
  let closestIdx = -1;

  for (let [i, point] of points.entries()) {
    let [_x, _y] = point;
    if (_x == x || _y == y) {
      let dist = Math.abs(x - _x) + Math.abs(y - _y);
      if (dist < closest) {
        closest = dist;
        closestIdx = i;
      }
    }
  }

  return closestIdx;
}

function main() {
  let x = 3;
  let y = 4;
  let points = [
    [1, 2],
    [3, 1],
    [2, 4],
    [2, 3],
    [4, 4],
  ];
  let result = nearestValidPoint(x, y, points);
  console.log(result);
}

main();
