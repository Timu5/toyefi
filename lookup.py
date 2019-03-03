

def lookup_1D(table, arg):

	start = table.axis[0]
	end = table.axis[15]
	
	if arg <= start:
		return table.data[0]
	elif arg >= end:
		return table.data[15]
		
	for i in range(len(table.axis)):
		if arg == table.axis[i]:
			return table.data[i]
		elif arg >= table.axis[i] and arg < table.axis[i]:
			delta1 = args - table.axis[i]
			delta2 = table.axis[i + 1] - args
			return (table.data[i] * delta1 + table.data[i + 1] * delta2) / (table.axis[i + 1] - table.axis[i])
			
	return 0
	
