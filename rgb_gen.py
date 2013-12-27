import random

foo = open("rgb.csv","w")

for i in range(0,500):
	R=random.randrange(0,255,1)
	G=random.randrange(0,255,1)
	B=random.randrange(0,255,1)
	if R > G+B:
		foo.write(str(R)+","+str(G)+","+str(B)+",1,1\n")
	else:
		foo.write(str(R)+","+str(G)+","+str(B)+",1,-1\n")
foo.close()
