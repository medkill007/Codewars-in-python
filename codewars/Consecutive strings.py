def longest_consec(strarr, k):
	s=""
	if (len(strarr)==0) or (k>len(strarr)) or (k <=0):
		return s
	
	x,y=0,0
	for i in range(len(strarr)):
		if len(strarr[i])>x:
			x=len(strarr[i])
			y=i
	n=y
	if k>=2:
		for i in range(k):
			if y+2>len(strarr):
				n-=1
			if len(strarr[n-1])>len(strarr[n]):
				n-=1
				print('WIN')
	for i in range(n,n+k):
		s+=strarr[i]
	return s

asd=int(input())
print(longest_consec(input().split(','),asd))