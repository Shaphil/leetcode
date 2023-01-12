/*
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Runtime: 90 ms
Memory: 46.3 MB
https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/876794764/
*/

class ListNode {
  val: number;
  children: ListNode[];
  constructor(val?: number) {
    this.val = val === undefined ? 0 : val;
    this.children = [];
  }
}

function preorder(root: ListNode | null): number[] {
  let pre: number[] = [];
  preorderRecursive(root, pre);
  return pre;
}

function preorderRecursive(root: ListNode | null, pre: number[]) {
  if (root) {
    pre.push(root.val);
    if (root.children) {
      for (let child of root.children) {
        preorderRecursive(child, pre);
      }
    }
  }
}

function main() {
  let tree = new ListNode(1);
  let childrenLevel_1 = [new ListNode(3), new ListNode(2), new ListNode(4)];
  let childrenLevel_2 = [new ListNode(5), new ListNode(6)];

  tree.children = childrenLevel_1;
  tree.children[0].children = childrenLevel_2;

  let result = preorder(tree);
  console.log(result);
}

main();
