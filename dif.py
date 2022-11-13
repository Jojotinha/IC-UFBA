#GRÁFICO DA DIFUSÃO VERSUS TEMPERATURA
#=======================================================
#=======================================================
import matplotlib.pyplot as plt
import numpy as np

info = open('info.txt')
for line in info:
	if line.startswith('T'):
		T = (line.split())[2:]
	elif line.startswith('Source'):
		path = (line.split())[2:]
	elif line.startswith('elements'):
		elements = (line.split())[2:]
print(T)
print(path)
for k in elements:
	print(k)
	name = input('Enter elements \n >>>').strip()
	file = (path[0] + 'msd\\' + 'dif{}.txt'.format(k))
	fhand = open(file)
	x = []
	y = []
	for lines in fhand:
		lines = lines.split()
		x.append(float(lines[0]))
		y.append(float(lines[1]))
	plt.plot(x,y,'r+',markersize = 10)
	m,b = np.polyfit(x,y,1)
	xo = np.linspace(min(x),max(x),2000)
	yo = m*xo + b
	plt.plot(xo,yo,linewidth = 1,color = 'black')
	plt.xlabel('Temperature (K)')
	plt.ylabel('D*10^-9 (m^2/s)')
	plt.title('Temperature dependance of self-diffusion coefficient of {} '.format(name))
	x = np.array(x)
	d = m*x + b
	print(x)
	print(d)		
	plt.savefig(path[0] + 'msd\\' + 'dif{}.png'.format(k))
#=======================================================
#=======================================================
