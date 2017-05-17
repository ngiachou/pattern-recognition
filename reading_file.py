def readFile(filename):
	foo = open(filename,"r")
	data = []
	for line in foo.readlines():
		v=map(int,line.strip("\n").split(","))
		data = data + [list(v)]
	return data
