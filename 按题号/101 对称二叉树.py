# 101.对称二叉树

#给定一个二叉树，检查它是否是镜像对称的。
#
#例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#	 1
#	/ \
#  2   2
# / \ / \
#3  4 4  3
#但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#	 1
#	/ \
#  2   2
#	\   \
#	3    3
#说明:
#
#如果你可以运用递归和迭代两种方法解决这个问题，会很加分。


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		flag = 0
		if root.left and root.right:
			if root.left == root.right:
				flag = self.isSymmetric(root.left)
				flag = self.isSymmetric(root.right)
				return flag
			else:
				return False
		if not root.left and not root.right:
			return 0
		else:
			return 1
		if not flag:
			return True
		else:
			return False
		

if __name__ == "__main__":
	pass