from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

length = 1
spalling_depth = 0.05

class PlotSpalling:

	def __init__(self,length,spalling_depth):
		self.length = float(length)
		self.spalling_depth_original = float(spalling_depth)
		self.spalling_depth_new = self.spalling_depth_original * self.length
		self.radious_original = 0
		self.radious_new = 0
		pass

	def calcRadious(self):
		self.radious_original = (self.spalling_depth_original**2 + self.length/4)/(2*self.spalling_depth_original)
		fraction_original = 1/self.radious_original
		self.radious_new = self.length/fraction_original
		print(self.radious_new)

	def calcZ(self):
		x = np.arange(-self.length/2,self.length/2,0.1)
		y = np.arange(-self.length/2,self.length/2,0.1)
		X,Y = np.meshgrid(x,y)	
		Z = (self.radious_new**2 - X**2 - Y**2)**0.5 - self.radious_new + self.spalling_depth_new
		return X, Y, Z

	def plotArea(self):
		X, Y, Z = PlotSpalling(self.length,self.spalling_depth_new).calcZ()

		for i in np.arange(len(X)):
		    for j in np.arange(len(Y)):
		        if Z[j,i] < 0:
		            Z[j,i] = 0
		        else:
		            pass


		fig = plt.figure(figsize=(18,3))
		ax = fig.add_subplot(111, projection='3d')

		ax.set_zlim([-0.5,0.5])

		# Plot a 3D surface
		ax.plot_surface(X, Y, Z, cmap=cm.jet,
		                       linewidth=0, antialiased=False)

		plt.show()

PlotSpalling(1,0.05).plotArea()