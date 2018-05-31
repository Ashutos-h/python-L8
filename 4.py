#Answer 4
class MovieDetails:
	def __init__(self,movie,artist,yor,rating):
		self.movie=movie
		self.artist=artist
		self.yor=yor
		self.rating=rating
	def display(self):
		print("Movie Name:", self.movie)
		print("Artist Name:", self.artist)
		print("Year of Release:", self.yor)
		print("Ratings:", self.rating)
	def addDeatils(self,universe):
		self.universe=universe
		print("Universe:", self.universe)
md=MovieDetails('Black Panther','Chadwick Boseman',2018,8.5)
md.display()
md.addDeatils('Marvel')

