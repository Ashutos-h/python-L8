#Answer 1
class Circle:
	def __init__(self,radius):
		self.radius=radius
	def getArea(self):
		return 3.142*self.radius*self.radius
	def getCircumference(self):
		return 2*3.142*self.radius
cir=Circle(5)
print("Area of circle:", cir.getArea())
print("Circumference of circle:", cir.getCircumference())
