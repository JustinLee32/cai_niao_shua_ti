# 464.我能赢吗

#在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。
#
#如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
#
#例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
#
#给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
#
#你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
#
#示例：
#
#输入：
#maxChoosableInteger = 10
#desiredTotal = 11
#
#输出：
#false
#
#解释：
#无论第一个玩家选择哪个整数，他都会失败。
#第一个玩家可以选择从 1 到 10 的整数。
#如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
#第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
#同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

#class Solution:
#	def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
		#choose = [i + 1 for i in range(maxChoosableInteger)]
		#flag= 1
		# 贪心策略：每次选取最小的数
		# 本次玩家取的时候，若该玩家赢：则当次的 max > 当前目标
		# 若该玩家输：则本次的 min + max >= 本次的目标 但是本次的 max < 本次目标
		# 所以在不能保证本次赢的前提下，想要尽量让对方输，也即下一次的 min + max - 下一次目标 要尽可能的大；并且也不能让对方赢，即下一次的max < 下一次的目标（这个好像始终是对的）
		# 故采取贪心策略：
		# 想要对手尽可能地输：每次取当前最大的数，这样才能使得下一次 min + max - 下一次的目标（尽可能大）
		# 该贪心策略可以经过推导得出
#		for _ in range(maxChoosableInteger):
#			if choose[-1] >= desiredTotal:
#				break
#			else:
#				desiredTotal -= choose[-1]
#				del choose[-1]
#				flag += 1
#		if flag % 2:
#			return True
#		else:
#			return False
			

#class Solution:
#	def canIWin(self,maxChoosableInteger: int, desiredTotal: int) -> bool:
#		if desiredTotal <= maxChoosableInteger:
#			return True
#		if not desiredTotal % (maxChoosableInteger + 1):
#			return False
#		elif desiredTotal % (maxChoosableInteger + 1) < maxChoosableInteger:
#			return True
#		else:
#			return not self.canIWin(maxChoosableInteger - 1, desiredTotal- maxChoosableInteger)


class Solution:
	def canIWin(self,maxChoosableInteger: int, desiredTotal: int) -> bool:
		if maxChoosableInteger >= desiredTotal:		
			return True
		if (1 + maxChoosableInteger) * maxChoosableInteger < desiredTotal:
			return False			
		def canWin(target: int, cache: int, maxChoosableInteger: int, dic) -> bool:
			if dic.get(cache):
				return dic[cache]
			for i in range(1, maxChoosableInteger+1):
				current = 1 << i
				if (current & cache) == 0 and (i >= target or canWin(target - i, current | cache, maxChoosableInteger, dic) == False):
					dic[current] = True
					return True
			dic[cache] = False
			return False
		dic = {}
		return canWin(desiredTotal, 0, maxChoosableInteger, dic)

		
		
if __name__ == "__main__":
	sol = Solution()
	print(sol.canIWin(18, 79))


# m,n
# 9/40: 30,20,10 False
# 9/39: 29,19,9 False -> m-1,n-m  # 8/30 21,12,3
# 9/38: 28,18,8 True
# 9/37: 27,17,7 True

# 10/40: 7,18,29,40	   6, 13,29
#					   11,22,33
# 7,8
# 4,3
# 9/39: 9,19,29,39,49
# 9,6,5
#   8,4,