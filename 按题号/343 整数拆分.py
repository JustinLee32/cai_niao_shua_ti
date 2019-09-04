class Solution:
	def integerBreak(self, n: int) -> int:
		if n <= 2:
			return 1
		if n == 3:
			return 2
		a = n // 3
		n -= 3*a
		if n%2:
			a -= 1; b = (n+3) //2
		else:
			b = n // 2
		return 2**b*3**a
if __name__ == "__main__":
	print(Solution.integerBreak(None, 6))