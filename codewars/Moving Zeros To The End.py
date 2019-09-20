def move_zeros(array):
	x=0
	for i in range(len(array)):
		if (array[i]=='0'):
			x+=1
	for i in range(1,x):
		for o in range(len(array)):
			if (array[i]=='0'):
				del array[i]
				array.append(0)
				break
	return array

print(move_zeros(input()).split(','))
		array.remove(0)
		array.append(0)

def move_zeros(array):
	x=0
	for i in range(len(array)):
		array[i]=str(array[i])
		'''if (str(array[i])=='0'):
			x+=1'''
	for i in range(x):
		array.remove(0)
		array.append(0)

	return array