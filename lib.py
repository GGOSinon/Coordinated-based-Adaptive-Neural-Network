class Vector3D():
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	def norm(self):
		return math.sqrt(x * x + y * y + z * z)

	def __add__(self, other):
		nx, ny, nz = self.x + other.x, self.y + other.y, self.z + other.z
		return Vector3D(nx, ny, nz)

	def __sub__(self, other):
		nx, ny, nz = self.x - other.x, self.y - other.y, self.z - other.z
		return Vector3D(nx, ny, nz)

	def __mul__(self, other):
		nx, ny, nz = other * self.x, other * self.y, other * self.z
		return Vector3D(nx, ny, nz)

