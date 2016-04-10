class Pid:
	
	def __init__(self,p,i,d,dt):
		
		self.p=p
		self.i=i
		self.d=d
		self.error_integral=0.0
		self.error_t_1=0.0
		self.dt=dt
	
	def controlSignal(self,error):
		
		#control signal using error at t, error integral in [0,t] and d(error)/dt at t=(error(t)-error(t_1))/dt
		error_derivative=(error-self.error_t_1)/self.dt
		control=self.p*error+self.i*self.error_integral+self.d*error_derivative
		
		#update error_integral and error_t_1 for next timestep
		self.error_integral+=error*self.dt
		self.error_t_1=error
		return control
"""
a=Pid(0.1, 0.3, 0.001, 0.1)
speed=0.0
ref_speed=50.0
count=0

while count<100:
	count+=1
	print 'iteration:%d,speed=%d'%(count,speed)
	error=ref_speed-speed
	speed=speed+a.controlSignal(error)
"""
