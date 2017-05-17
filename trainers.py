""" A class for training our perceptrons """
class Trainers:
	""" Constructor """
	def __init__(self, data, r=1):
		self.data_vectors = data # training dataset
		self.r = r
		self.wrong_classified_vectors = ["dummy"]

	def gradientDescent(self, perceptron):
		print ("Begin training...")
		last = len(self.data_vectors[0])-1
		t = 0
		# As long we have wrong classified vectors training is not complete
		while self.wrong_classified_vectors != []:
			self.wrong_classified_vectors = []
			# For each vector in training dataset we check the classifier
			for i in range(len(self.data_vectors)):
				if self.data_vectors[i][last]*perceptron.fire(self.data_vectors[i][:last]) < 0: # Wrong classification
					self.wrong_classified_vectors = self.wrong_classified_vectors + [self.data_vectors[i]]
			# Now that we have all the wrong classified vectors (or none)
			# lets calculate the new weight vector
			if self.wrong_classified_vectors == []:
				break
			new_weight_vector = perceptron.getWeightVector()
			# For each wrong vector
			error = [ self.wrong_classified_vectors[0][last]*x for x in self.wrong_classified_vectors[0][:last]]
			for wr_v in self.wrong_classified_vectors[1:]:
				#print wr_v
				#print error
				#raw_input()
				for index in range(len(wr_v[:last])):
					error[index] = error[index] + wr_v[last]*wr_v[index]
			new_weight_vector = [y + self.r*x for y,x in zip(new_weight_vector,error)]
			perceptron.setWeightVector(new_weight_vector)
			#print "Data "+str(self.data_vectors)
			#print "Wrong Classified Vectors "+str(self.wrong_classified_vectors)
			#print "Current weight vector "+str(new_weight_vector)
			#print "Itteration "+str(t)
			t += 1
			#raw_input("Press Enter:>")
		return perceptron
