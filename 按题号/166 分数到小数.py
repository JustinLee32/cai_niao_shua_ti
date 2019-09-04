# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 示例 1:
#
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 示例 2:
#
# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 示例 3:
#
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
#


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        zheng = numerator // denominator
        numerator = (numerator % denominator) * 10
        if not numerator:
            return str(zheng)
        xiao = ""
        dic = {}
        index = 0
        while True:
            quotient = numerator // denominator
            numerator = numerator % denominator
            if not numerator:
                return '.'.join([str(zheng), xiao + str(quotient)])
            if numerator in dic:
                xiao += str(quotient)
                break
            else:
                dic[numerator] = index
                index += 1
                xiao += str(quotient)
                numerator = numerator * 10
        xiao = xiao[:dic[numerator]+1] + '(' + xiao[dic[numerator]+1:] + ')'
        res = '.'.join([str(zheng), xiao])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(1, 3))
