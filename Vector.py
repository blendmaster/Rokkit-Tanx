from math import *

class Vector:
	"""A 2d x,y vector, useful especially for velocity"""

	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)

	def setVector(self, v):
		self.x = float(v.x)
		self.y = float(v.y)

	def getUnitVector(self):
		if self.getMagnitude() != 0:
			return Vector( self.x / self.getMagnitude(), self.y / self.getMagnitude() )
		else:
			return Vector(0.0,0.0)
		
	def multiply(self,s):
		return Vector( self.x * s, self.y * s )

	def getMagnitude(self):
		return sqrt( self.x**2 + self.y**2 )

	def getDirection(self):
		#this is in radians, desho?
		return atan2(self.y,self.x)

	def add(self, v):
		return Vector( self.x + v.x, self.y + v.y )
	
	def dotProduct(self, v):
		return self.x*v.x + self.y*v.y
	
	def crossProduct(self,v):
		# this is just the magnitude, mmkay?
		return self.getMagnitude()*v.getMagnitude()*sin( self.getDirection() - v.getDirection() )

	def __str__(self):
		return "Vector("+str(self.x)+","+str(self.y)+")"




# testing
##if __name__ == "__main__":
##	v = Vector(2,5)
##	print v
##	v.add(Vector( 2,5) )
##	print v
##	print v.crossProduct(Vector(3,6))
##	print v.getMagnitude()
