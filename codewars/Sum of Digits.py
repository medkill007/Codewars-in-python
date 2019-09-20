def digital_root(n):
	while True:
		x=list(str(n))
		if len(x)==1:
			return n
		else:
			n=0
			for i in x:
				n+=int(i)
print(digital_root(int(input())))