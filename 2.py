#Answer 2
class Student:
	def __init__(self,name,rno):
		self.name=name
		self.rno=rno
	def display(self):
		print("Name:", self.name)
		print("Roll No:", self.rno)
	def setAge(self,age):
		self.age=age
		print("Age:", self.age)
	def setMarks(self,marks):
		self.marks=marks
		print("Marks:", self.marks)
stud=Student('Ashu',123)
stud.display()
stud.setAge(10)
stud.setMarks(100)
