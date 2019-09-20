def count_smileys(arr):
	def search(x):
		for i in eye:
			if i==x:
				return 1
		for i in nose:
			if i==x:
				return 2
		for i in mouth:
			if i==x:
				return 3
		return False
	eye=[':',';']
	nose=['-','~']
	mouth=[')','D']

	for i in range(len(arr)):
		asd=[]
		for o in arr[i]:
			y=search(o)
			asd.append(y)
			if y==False:
				arr[i]=''
				break
		if (asd!=[1,3]) and (asd!=[1,2,3]):
			arr[i]=''

	x=0
	for i in range(len(arr)):
		if arr[i]=='':
			x+=1
	for i in range(x):
		arr.remove('')
	return len(arr)
print(count_smileys(input().split(' ')))
