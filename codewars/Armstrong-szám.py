def narcissistic(value):
	v=list(str(value))
	x=len(v)
	for i in range(x):
		v[i]=int(v[i])**x
	return True if sum(v)==value else False



print(narcissistic(int(input())))