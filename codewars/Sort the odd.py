def sort_array(source_array):
	odd=[]
	for i in range(len(source_array)):
		if int(source_array[i])%2==1:
			odd.append(source_array[i])
			source_array[i]=''
	odd=sorted(odd)
	for i in range(len(source_array)):
		if source_array[i]=='':
			source_array[i]=odd[0]
			del odd[0]
	return source_array
print(sort_array(list(str(input()))))