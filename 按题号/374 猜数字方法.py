# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
#
# -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！
# 示例 :
#
# 输入: n = 10_7 周赛.5 双周赛, pick = 6
# 输出: 6


def guess(num: int, pick=6):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = int((left + right) / 2)
        while right - left > 1:
            if guess(mid) == -1:
                right = mid
                mid = int((left + right) / 2)
            elif guess(mid) == 0:
                return mid
            else:
                left = mid
                mid = int((left + right) / 2)
        return left if not guess(left) else right


if __name__ == '__main__':
    sol = Solution()
    print(sol.guessNumber(10))
