#编写一个程序，找出第 n 个丑数。
#
#丑数就是只包含质因数 2, 3, 5 的正整数。
#
#示例:
#
#输入: n = 10
#输出: 12
#解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#说明:  
#
#1 是丑数。
#n 不超过1690。

class Solution:
	def nthUglyNumber(self, n: int) -> int:
		res = [1]
		i = 0 
		j = 0
		k = 0 # 理解：三个指针分别指向2，3，5所要乘的位置
		for _ in range(n-1):
			res.append(min(res[i] * 2, res[j] * 3, res[k] * 5))
			#三个if要并列，这样才能避免重复的情形
			if res[-1] == res[i] * 2:
				i += 1
			if res[-1] == res[j] * 3:
				j += 1
			if res[-1] == res[k] * 5:
				k += 1
		return res[-1]
		
	def nthUglyNumber_1(self, n: int) -> int:
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
			k = 0; num = 0;
			while k < n:
				num += 1
				if isUgly(num):
					k += 1
			return num
	
	
if __name__ == "__main__":
	print(Solution.nthUglyNumber(None,315))
	
