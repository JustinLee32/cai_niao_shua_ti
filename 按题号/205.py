s = "abaa"
t = "bcdd"
flag = 1
dic1 = {}
if len(s) <= 1:
	print("True")
dic1[s[0]] = t[0]
for i in range(1,len(s)):
	if s[i] not in dic1 and t[i] not in t[:i]:
		dic1[s[i]] = t[i]
	elif s[i] in dic1 and dic1[s[i]]==t[i]:
		continue
	else:
		flag = 0
		break
if flag == 0:
	print("False")
else:
	print("True")
