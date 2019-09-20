def countBits(n):
	asd=0
	while n!=0:
		if n%2==1:
			n-=1
			asd+=1
		n/=2
	return asd
print(countBits(int(input())))
