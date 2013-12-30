import random

foo = open("rgb_test.csv","w")

for i in range(0,20000):
	R=random.randrange(0,255,1)
	G=random.randrange(0,255,1)
	B=random.randrange(0,255,1)
	if R > G+B:
		foo.write(str(R)+","+str(G)+","+str(B)+",1,1\n")
	else:
		foo.write(str(R)+","+str(G)+","+str(B)+",1,-1\n")
foo.close()
