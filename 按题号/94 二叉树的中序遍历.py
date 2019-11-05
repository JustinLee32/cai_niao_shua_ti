# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []

        def _recursion(now):
            if now.left:
                self.inorderTraversal(now.left)
            self.ans.append(root.val)
            if now.right:
                self.inorderTraversal(now.right)
        _recursion(root)
        return self.ans


if __name__ == '__main__':
    nums = [1, None, 2, 3]
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = 3
    root.right.right = None
    sol = Solution()
    print(root)
    # print(sol.inorderTraversal(root))
    