from perceptron import *
from reading_file import *
from trainers import *

p = Perceptron([1,1,1,1])
print "Testing perceptron with weight vector: "+str(p.getWeightVector())
print "Result for input vector (255,100,30,1): "+str(p.fire([255,100,30,1]))
print "Result for input vector (200,110,50,1): "+str(p.fire([200,110,50,1]))
print "Result for input vector (30,100,200,1): "+str(p.fire([30,100,200,1]))
print "Result for input vector (120,235,12,1): "+str(p.fire([120,235,12,1]))
print "Result for input vector (40,100,30,1): "+str(p.fire([40,100,30,1]))
print "Result for input vector (155,55,100,1): "+str(p.fire([155,55,100,1]))
print "Result for input vector (255,200,55,1): "+str(p.fire([255,200,55,1]))

data = readFile("rgb.csv")
# for debugging
# print data
t = Trainers(data,0.7)
raw_input("Continue?")
t.gradientDescent(p)
print "Perceptron's weight vector after training: "+str(p.getWeightVector())
