

class Person:
	def __init__(self, name):
		self._name = name

	def greeting(self):
		print("Hello, I am " + str(self._name))

	def get_name(self):
		return self._name


daniel = Person("Daniel")
daniel.greeting()

