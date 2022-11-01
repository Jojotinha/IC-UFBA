import matplotlib.pyplot as plt
import numpy as np
file = ('dif_temp.txt')
fhand = open(file)
x = []
y = []
for lines in fhand:
	lines = lines.split()
	print(lines)
	x.append(float(lines[0]))
	y.append(float(lines[1]))
plt.plot(x,y,'r+',markersize = 10)
m,b = np.polyfit(x,y,1)
xo = np.linspace(min(x),max(x),2000)
yo = m*xo + b
plt.plot(xo,yo,linewidth = 1,color = 'black')
plt.xlabel('Temperature (K)')
plt.ylabel('D*10^-9 (m^2/s)')
plt.title('Temperature dependance of self-diffusion coefficient')
x = np.array(x)
d = m*x + b
print(x)
print(d)		
plt.savefig('dif_plot.png')
