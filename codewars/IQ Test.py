def iq_test(numbers):
	def asd(x,y):
		for i in range(len(x)):
			n=int(x[i])
			if (n%2==y):
				return i+1
	odd,even=0,0

	numbers=numbers.split(' ')
	for i in range(len(numbers)):
		n=int(numbers[i])
		if (n%2==0):
			even+=1
		else:
			odd+=1
	if even==1:
		return asd(numbers,0)
				
	if odd==1:
		return asd(numbers,1)
	return -1