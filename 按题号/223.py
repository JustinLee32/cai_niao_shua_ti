#233.矩形面积
#在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
#
#每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
#
#
#
#示例:
#
#输入: -3, 0, 3, 4, 0, -1, 9, 2
#输出: 45

class Solution:
	def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
		x_1 = max(A,E)
		y_1 = max(B,F)
		x_2 = min(C,G)
		y_2 = min(D,H)
		S = (C - A) * (D - B) + (G - E) * (H - F)
		if x_2 > x_1 and y_2 > y_1:
			return(S - (x_2 - x_1) * (y_2 - y_1))
		else:
			return S
			
if __name__ == '__main__':
	print(Solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))