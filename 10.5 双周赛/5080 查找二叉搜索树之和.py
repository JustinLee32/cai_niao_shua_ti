# 给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。
#
# 如果可以找到返回 True，否则返回 False。




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = False

    def _helper(self, tree1: TreeNode, tree2: TreeNode, target: int):
        if not tree2:
            return
        if self.ans:
            return
        else:
            if tree1.val + tree2.val > target:
                self._helper(tree1, tree2.left, target)
            elif tree1.val + tree2.val == target:
                self.ans = True
                return
            elif tree1.val + tree2.val < target:
                self._helper(tree1, tree2.right, target)

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        self.root2 = root2

        def _recursive(tree1: TreeNode, tree2: TreeNode, target: int):
            if self.ans:
                return
            if not tree1:
                return
            else:
                self._helper(tree1, self.root2, target)
                if not self.ans:
                    _recursive(tree1.left, self.root2, target)
                    _recursive(tree1.right, self.root2, target)

        _recursive(root1, root2, target)
        return self.ans


if __name__ == '__main__':
    pass

