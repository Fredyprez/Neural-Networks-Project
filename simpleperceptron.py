from numpy import random
from matplotlib import pyplot as plt

def sign(n):
	if n >= 0: return 1
	else: return -1

class Perceptron:
	def __init__(self):
			self.weights = random.uniform(-1.0, 1.0, 2)
			self.learningRate = .1
			
	def guess(self, inputs):
		sum = 0
		for i in range(0,len(self.weights)):
			sum += inputs[i] * self.weights[i]
			output = sign(sum)
		return output 

	def __str__(self):
		for i in self.weights:
			print(f"weight: {i}")
		return f""
	def train(self, inputs, target):
		guess = self.guess(inputs)
		error = target - guess
		for i in range(0,len(self.weights)):
			self.weights[i] += error * inputs[i] * self.learningRate
		return guess
