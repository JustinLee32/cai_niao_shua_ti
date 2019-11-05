# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
#
# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
#
# 示例 1：
#
# 输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
# 示例 2：
#
# 输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
# 示例 3：
#
# 输入：n = 5
# 输出：68

# 提示：
#
# 1 <= n <= 2 * 10^4

from typing import List


class MatrixMultiply:
    def __init__(self):
        pass

    def matrix_multiply(self, matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
        matrix_c = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
        for i in range(len(matrix_c)):
            for j in range(len(matrix_c[0])):
                for k in range(len(matrix_b)):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return matrix_c


class EyesMatrix:
    def __init__(self):
        pass

    def generate_eyes_matrix(self, size: int) -> List[List[float]]:
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            matrix[i][i] = 1
        return matrix


class FastExponentiationOfMatrix(MatrixMultiply, EyesMatrix):
    def __init__(self, matrix: List[List[float]], power: int):
        # 做矩阵快速幂运算要求为方阵
        self.matrix = matrix
        self.power = power
        super(MatrixMultiply).__init__()
        super(MatrixMultiply).__init__()

    def matrix_fast_exponentiation(self):
        def _recursion(matrix: List[List[float]], power: int) -> List[List[float]]:
            if not power:
                return self.generate_eyes_matrix(len(self.matrix))
            # if power < 0:

            if power == 1:
                return matrix
            temp_1 = _recursion(matrix, power // 2)
            temp_2 = self.matrix_multiply(temp_1, temp_1)
            if power & 1:
                return self.matrix_multiply(matrix, temp_2)
            else:
                return temp_2

        return _recursion(self.matrix, self.power)


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        matrix = [[0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0]]
        power = n - 1
        vector = [[1, 1, 1, 1, 1]]
        feom = FastExponentiationOfMatrix(matrix, power)
        cache = feom.matrix_fast_exponentiation()
        res = feom.matrix_multiply(vector, cache)
        return sum(feom.matrix_multiply(vector, cache)[0]) % (10 ** 9 + 7)


# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         dp = [[0 for _ in range(5)] for _ in range(n)]
#         for j in range(5):
#             dp[0][j] = 1
#         for i in range(1, n):
#             for j in range(5):
#                 if j == 0:
#                     dp[i][j] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
#                 elif j == 1:
#                     dp[i][j] = dp[i-1][0] + dp[i-1][2]
#                 elif j == 2:
#                     dp[i][j] = dp[i-1][1] + dp[i-1][3]
#                 elif j == 3:
#                     dp[i][j] = dp[i-1][2]
#                 elif j == 4:
#                     dp[i][j] = dp[i-1][2] + dp[i-1][3]
#         return sum(dp[-1]) % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countVowelPermutation(n=5))
