""" A class for training our perceptrons """
class Trainers:
	""" Constructor """
	def __init__(self, data, r=1):
		self.data_vectors = data # training dataset
		self.r = r
		self.wrong_classified_vectors = ["dummy"]

	def gradientDescent(self, perceptron):
		last = len(self.data_vectors[0])-1
		# As long we have wrong classified vectors training is not complete
		while self.wrong_classified_vectors == []:
			self.wrong_classified_vectors = []
			# For each vector in training dataset we check the classifier
			for i in range(len(self.data_vectors)):
				if self.data_vectors[i][last]*perceptron.fire(self.data_vectors[i][:last]) < 0: # Wrong classification
					self.wrong_classified_vectors = self.wrong_classified_vectors + [self.data_vectors[i][:last]]
				new_weight_vector = []
				#TODO complete the algorithm
				for item in perceptron.getWeightVector():
					new_weight_vector = new_weight_vector + [ item + self.r*sum([self.data_vectors[i][last]*x for x in self.data_vectors[i][:last]]) ]
				perceptron.setWeightVector(new_weight_vector)
