# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import defaultdict
        self.level_sum_dict = defaultdict(int)
        ans = 1

        def _recursion(father: TreeNode, level: int):
            if not father:
                return
            else:
                self.level_sum_dict[level] += father.val
                _recursion(father.left, level + 1)
                _recursion(father.right, level + 1)

        _recursion(root, 1)
        temp = self.level_sum_dict[1]
        for key, value in self.level_sum_dict.items():
            if value > temp:
                ans = key
                temp = value
        return ans


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':
    s = input()
    root = stringToTreeNode(s)
    sol = Solution()
    print(sol.maxLevelSum(root))


