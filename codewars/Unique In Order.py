def unique_in_order(iterable):
    iterable=list(iterable)
    for o in range((len(iterable))-1):
    	for i in range((len(iterable))-1):
    		if iterable[i]==iterable[i+1]:
    			del iterable[i]
    			break
    	
    return iterable

print(unique_in_order(input()))