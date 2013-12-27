""" This is a class to implement the perceptron artificial nueron """
class Perceptron:

	def __init__(self, w_v=[0]):
		self.weight_vector = w_v
	""" Geter for weight vector """
	def getWeightVector(self):
		return self.weight_vector
	""" Seter for weight vector """
	def setWeightVector(self,w_v):
		self.weight_vector = w_v
	
	def fire_fnc(self,input_vector):
		suma = 0
		for index in range(len(input_vector)):
			suma += self.weight_vector[index]*input_vector[index]
		return self.step_fnc(suma)
	
	def step_fnc(self,suma):
		if suma > 0:
			return 1
		else:
			return -1
	
	def fire(self,input_vector):
		return self.fire_fnc(input_vector)
