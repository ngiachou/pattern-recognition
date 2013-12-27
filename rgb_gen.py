import random

foo = open("rgb.csv","w")

foo.write("R,G,B\n")
for i in range(0,100):
	foo.write(str(random.randrange(0,255,1))+","+str(random.randrange(0,255,1))+","+str(random.randrange(0,255,1))+"\n")
foo.close()
