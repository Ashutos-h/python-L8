#Answer 3
class Temperature:
	def convertFahrenheit(self,cels):
		self.fahren=((9*cels)/5)+32
		print("Fahrenheit Degree:", self.fahren)
	def convertCelsius(self,fahren):
		self.cels=((fahren-32)/9)*5
		print("Celsius Degree:", self.cels)
temp=Temperature()
temp.convertFahrenheit(30)
temp.convertCelsius(100)