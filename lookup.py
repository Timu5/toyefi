class Table1D:
	def __init__(self):
		self.axis = [x for x in range(16)]
		self.data = [0 for x in range(16)]
		
class Table2D:
	def __init__(self):
		self.axis = [[y for y in range(16)] for x in range(2)]
		self.data = [[0 for y in range(16)] for x in range(16)]

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
		elif arg >= table.axis[i] and arg < table.axis[i + 1]:
			delta1 = args - table.axis[i]
			delta2 = table.axis[i + 1] - args
			return (table.data[i] * delta1 + table.data[i + 1] * delta2) // (table.axis[i + 1] - table.axis[i])

	return 0

def lookup_2D(table, x, y):

	if x < table.axis[0][0]:
		x = table.axis[0][0]
	elif x > table.axis[0][15]:
		x = table.axis[0][15]

	if y < table.axis[1][0]:
		y = table.axis[1][0]
	elif y > table.axis[1][15]:
		y = table.axis[1][15]

	valuex = 0
	valuey = 0
	deltax0 = 0
	deltax1 = 0
	deltay0 = 0
	deltay1 = 0

	for i in range(len(table.axis[0]) - 1):
		if x >= table.axis[0][i] and x < table.axis[0][i + 1]:
			valuex = i
			deltax0 = x - table.axis[0][i]
			deltax1 = table.axis[0][i + 1] - x

	for i in range(len(table.axis[1]) - 1):
		if y >= table.axis[1][i] and y < table.axis[1][i + 1]:
			valuey = i
			deltay0 = y - table.axis[1][i]
			deltay1 = table.axis[1][i + 1] - y


	a = (table.data[valuex][valuey] * deltax0 + table.data[valuex + 1][valuey] * deltax1) // (table.axis[0][valuex] - table.axis[0][valuex + 1])
	b = (table.data[valuex][valuey + 1] * deltax0 + table.data[valuex + 1][valuey + 1] * deltax1) // (table.axis[0][valuex] - table.axis[0][valuex + 1])

	return (a * deltay0 + b * deltay1) // (table.axis[1][valuey] - table.axis[1][valuey + 1])


