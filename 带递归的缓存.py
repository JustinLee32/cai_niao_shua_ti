def fib(n, cache=None):
	if cache == None:
		cache = {}
	if n in cache:
		return cache[n]
	if n <= 1:
		return 1
	cache[n] = fib(n-1, cache) + fib(n-2, cache)
	return cache[n]


def myfib(n):
	if n <= 1:
		return 1
	else:
		return myfib(n-1) + myfib(n-2)

##########################################
# 使用函数装饰器生成包裹函数，将缓存机制变成外延 #
##########################################


def cache(func):
	data_cache = {}

	def wrap(*args):
		if args not in data_cache:
			data_cache[args] = func(*args)
		return data_cache[args]
	return wrap


@cache
def nb_fib(n):
	if n <= 1:
		return n 
	return nb_fib(n-1) + nb_fib(n-2)


if __name__ == "__main__":
	print(nb_fib(5))
