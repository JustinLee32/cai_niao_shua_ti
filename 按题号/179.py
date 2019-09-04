a = [0,0]
temp = []
ans = []
for i in range(len(a)):
	a[i] = str(a[i])
ans.append(a[0])
for i in range(1,len(a)):
	for j in range(i+1):
		temp.append(int(("".join(ans[:i-j])+a[i]+"".join(ans[i-j:]))))
	ans.insert(i-temp.index(max(temp)),a[i])	
	temp = []
print(str(int("".join(ans))))