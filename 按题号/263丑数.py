#编写一个程序判断给定的数是否为丑数。
#
#丑数就是只包含质因数 2, 3, 5 的正整数。
#
#示例 1:
#
#输入: 6
#输出: true
#解释: 6 = 2 × 3
#示例 2:
#
#输入: 8
#输出: true
#解释: 8 = 2 × 2 × 2
#示例 3:
#
#输入: 14
#输出: false 
#解释: 14 不是丑数，因为它包含了另外一个质因数 7。

class Solution:
	def isUgly(num: int) -> bool:
		if num == 0:
			return False
		while not num % 5:
			num = num // 5
		while not num % 3:
			num = num // 3
		while not num % 2:
			num = num // 2
		if num == 1:
			return True
		else:
			return False

if __name__ == "__main__":
	print(Solution.isUgly(-2147483648))