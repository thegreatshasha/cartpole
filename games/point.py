
class Point:
	
	def __init__(self,radius):
		self.x=0.0
		self.y=0.0
		self.vx=0.0
		self.vy=0.0
		self.radius=0,0

	def setPoint(self,x,y,vx,vy):
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy

	def getPoint(self):
		return self.x,self.y,self.vx,self.vy

