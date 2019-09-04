# 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
#
# 示例 1:
#
# 输入: a = 2, b = [3]
# 输出: 8
# 示例 2:
#
# 输入: a = 2, b = [1,0]
# 输出: 1024


class Solution:
    def superPow(self, a: int, b: list) -> int:
        r = 1
        a %= 1337
        for i in b:
            r = pow(r, 10) * pow(a, i) % 1337
        return r


if __name__ == '__main__':
    sol = Solution()
    print(sol.superPow(2, [1, 0]))

