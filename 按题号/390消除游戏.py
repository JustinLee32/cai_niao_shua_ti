#390消除游戏
#给定一个从1 到 n 排序的整数列表。
#首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
#第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
#我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
#返回长度为 n 的列表中，最后剩下的数字。
#
#示例：
#
#输入:
#n = 9,
#1 2 3 4 5 6 7 8 9
#2 4 6 8
#2 6
#6
#
#输出:
#6

#class Solution:
#	def __init__(self, n):
#		self.num = n
#	
#	def lastRemaining(self, mylist) -> int:
#		if len(mylist) == 1:
#			return mylist[0]
#		else:
#			del mylist[::2]
#			mylist.reverse()
#		return self.lastRemaining(mylist)
#		
#		
#		
#if __name__ == "__main__":
#	n = int(input())
#	sol = Solution(n)
#	print(sol.lastRemaining(list(range(1,n+1))))
	
	
	
class Solution:
	def lastRemaining(self, n: int) -> int:
		mylist = list(range(1,n+1))
		return self.mylastRemaining(mylist)
		
	def mylastRemaining(self, mylist):
		if len(mylist) == 1:
			return mylist[0]
		else:
			del mylist[::2]
			mylist.reverse()
		return self.mylastRemaining(mylist)
		

if __name__ == "__main__":
	sol = Solution()
	print(sol.lastRemaining(100000000))