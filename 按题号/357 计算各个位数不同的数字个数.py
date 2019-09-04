# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
#
# 示例:
#
# 输入: 2
# 输出: 91
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        temp_list = []
        for i in range(1, 11):
            temp_list.append(self._fact(i))
        if n <= 10:
            return sum(temp_list[:n])
        else:
            return sum(temp_list)

    def _fact(self, num):
        if num == 1:
            return 10
        res = 9
        for i in range(2, num + 1):
            res = res * (11 - i)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(0))
