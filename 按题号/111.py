import math
s=input();flag1=0
while s:
	flag1=1
	a="";b="";flag=0;e=[]
	for i in range(len(s)):
		if s[i]!=" " and flag==0:
			a+=s[i]
		elif s[i]!=" " and flag==1:
			b+=s[i]
		elif s[i]==" ":
			flag=1
	c=float(a);d=int(b);
	e.append(c)
	if d==0:
		print(round(0),2)
	elif d==1:
		print('%.2f' %sum(e))
	else:
		for i in range(2,d+1):
			e.append(math.sqrt(e[-1]))
		print('%.2f' %sum(e))
	s=input()
if flag1==0:
	print(round(0),2)
