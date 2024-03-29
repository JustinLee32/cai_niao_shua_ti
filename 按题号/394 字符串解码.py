# -*- coding: UTF-8 -*-
# Edit on July 25th, 2019

# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
# 示例:
#
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".


class Solution:
	def __init__(self):
		self.stack = []

	def decodeString(self, s: str) -> str:
		for i in range(len(s)):
			self.stack.append(s[i])
			if s[i] == ']':
				self.stack.extend(self.get_unit())
		return ''.join(self.stack)

	def get_unit(self):
		temp = ''
		res = []
		while self.stack:
			cache = self.stack.pop()
			if cache == '[':
				temp += cache
				break
			else:
				temp += cache
		temp = temp[::-1]
		temp = temp[1:-1:1]
		for i in range(len(temp)):
			res.append(temp[i])
		num = ''
		while self.stack:
			cache = self.stack.pop()
			if '0' <= cache <= '9':
				num += cache
			else:
				self.stack.append(cache)
				break
		num = int(num[::-1])
		return res * num


if __name__ == "__main__":
	sol = Solution()
	print(sol.decodeString("3[a2[c]]"))
