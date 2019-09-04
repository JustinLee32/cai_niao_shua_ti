# 171 Excel表列序号

#给定一个Excel表格中的列名称，返回其相应的列序号。
#
#例如，
#
#	A -> 1
#	B -> 2
#	C -> 3
#	...
#	Z -> 26
#	AA -> 27
#	AB -> 28 
#	...
#

class Solution:
	def titleToNumber(self, s: str) -> int:
		s = s[::-1]; res = 0
		for i in range(len(s)):
			res += (ord(s[i]) - 64) * 26 ** i  # A的Ascii码值为64
		return res
		
if __name__ == "__main__":
	print(Solution.titleToNumber(None, "ZY"))