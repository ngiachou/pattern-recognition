from perceptron import *
from reading_file import *

p = Perceptron([1,-1,-1])
print "Result: "+str(p.fire([255,100,30]))
print "Result: "+str(p.fire([100,100,30]))

data = readFile("rgb.csv")

print data
