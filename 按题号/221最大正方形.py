#在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
#示例:
#
#输入: 
#
#1 0 1 0 0
#1 0 1 1 1
#1 1 1 1 1
#1 0 0 1 0
#
#输出: 4

class Solution:
	#def maximalSquare(self, matrix: List[List[str]]) -> int:
	def maximalSquare(self, matrix) -> int:
		if not matrix: return 0  # matrix = []
		m = len(matrix); n = len(matrix[0])
		dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
		if m <= 1 or n <= 1:
			dp_2 = [[int(matrix[i][j]) for i in range(m)] for j in range(n)]
			return max(max(dp[0]), max(dp_2[0]))
		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = dp[i][j] * (1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]))
		# dp[i][j]表示以matrix[i][j]为正方形的右下角顶点所能够构成的最大正方形的边长
		res = 0
		for i in range(m):
			for j in range(n):
				res = max(res, dp[i][j])
		return res * res



if __name__ == "__main__":
#	matrix = input()
#	print(Solution.maximalSquare(None, matrix))
	print(Solution.maximalSquare(None, [
										 [1, 0, 1, 0, 0]
										,[1, 0, 1, 1, 1]
										,[1, 1, 1, 1, 1]
										,[1, 0, 0, 1, 0]
										]))	