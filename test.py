from perceptron import *
from reading_file import *
from trainers import *

def tester(p, data):
	output_string = ''
	last = len(data[0])-1
	true_positive = 0
	false_positive = 0
	true_negative = 0
	false_negative = 0
	for v in data:
		#print v
		#raw_input()
		if v[last] == 1:
			if v[last] == p.fire(v[:last]):
				true_positive += 1
			else:
				print (v)
				false_negative += 1
		else:
			if v[last] == p.fire(v[:last]):
				true_negative += 1
			else:
				print (v)
				false_positive += 1
	output_string += "Test  results\n"
	output_string += "true  positive: " + str(true_positive) + '\n'
	output_string += "true  negative: " + str(true_negative) + '\n'
	output_string += "false positive: " + str(false_positive) + '\n'
	output_string += "false negative: " + str(false_negative) + '\n'
	output_string += "Summation     : " +\
	str(true_positive + true_negative + false_positive + false_negative) + '\n'

	return output_string

if __name__ == '__main__':
	p = Perceptron([1,1,1,1])
	print ("Testing perceptron with weight vector: "+str(p.getWeightVector()))
	print ("Result for input vector (255,100,30,1): "+str(p.fire([255,100,30,1])))
	print ("Result for input vector (200,110,50,1): "+str(p.fire([200,110,50,1])))
	print ("Result for input vector (30,100,200,1): "+str(p.fire([30,100,200,1])))
	print ("Result for input vector (120,235,12,1): "+str(p.fire([120,235,12,1])))
	print ("Result for input vector (40,100,30,1): "+str(p.fire([40,100,30,1])))
	print ("Result for input vector (155,55,100,1): "+str(p.fire([155,55,100,1])))
	print ("Result for input vector (255,200,55,1): "+str(p.fire([255,200,55,1])))

	data = readFile("rgb.csv")
	# for debugging
	# print data
	t = Trainers(data,0.7)
	#raw_input("Continue?")
	t.gradientDescent(p)
	print ("Perceptron's weight vector after training: "+str(p.getWeightVector()))

	data = readFile("rgb_test.csv")
	print(tester(p,data))
