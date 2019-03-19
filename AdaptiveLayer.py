from lib import Vector3D

class AdaptiveNeuron():
	def __init__(self, r, b):
		self.r = r
		self.b = b
		self.Z = 0

	def actFunc(self, x):
		if x<0: return 0
		return x

	def dactFunc(self, x):
		if x<0: return 0
		return 1

	def forward(self, prevLayer):
		self.A = self.actFunc(self.Z)
		for prev_neuron in self.prevLayer.neurons: 
			r0 = prev_neuron.r
			dr = r - r0
			in_signal = prev_neuron.A / dr.norm()
			self.Z += in_signal

	def backpropagate(self, prevLayer, nextLayer):
		self.dZdr = Vector3D(0, 0, 0)
		self.dCdA = 0
		for prev_neuron in prevLayer.neurons:
			r0, A0 = prev_neuron.r, prev_neuron.A
			dr = self.r - r0
			self.dZdr += (A0 / (dr.norm()**3)) * dr
		for next_neuron in nextLayer.neurons:
			r0, dCdZ = next_neuron.r, next_neuron.dCdZ
			dr = self.r - r0
			self.dCdA += dCdZ / dr.norm()
		self.dCdZ = self.dCdA * self.dactFunc(self.Z)
			

class AdaptiveLayer():
	def __init__(self, prevLayer, num_neuron, z):
		self.prevLayer = prevLayer
		self.neurons = []
		for _ in range(num_neuron):
			neuron = AdaptiveNeuron(z)
			self.neurons(z)

	def forward(self):
		for neuron in self.neurons:
			x, y, z = neuron.x, neuron.y, neuron.z
			neuron.value = 0
			def backpropagate():
		for neuron in self.neurons:
			x, y, z = neuron.x, neuron.y, neuron.z
			neuron.value = 0
			for prev_neuron in self.prevLayer.neurons:
							
