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
	symbol = input('Enter the elements \n >>>).strip()
	for i in T:
		x = []
		y = []
		file = path[0] + 'msd\\' + 'msd-{}{}.dat'.format(k,i) 
		fhand = open(file) #abrindo o arquivo correspondente a temperatura i 
	# extraindo o x e o y 
		for line in fhand:
			line = line.split()
			try:
				float(line[0])
			except:
				continue
			x.append(float(line[0])*10**-15)
			y.append(float(line[1])*10**-20)
	#criando o grafico
		plt.plot(x,y,'r+',markersize = 8, label = 'Calculated MSD')
		m,b = np.polyfit(x,y,1)
		xo = np.linspace(min(x),max(x),2000)
		yo = m*xo + b
		plt.plot(xo,yo,linewidth = 1,color = 'black',label = 'Fit MSD'.format(k))
		plt.legend(loc = 'upper left')
		plt.ticklabel_format(axis = 'x',style = 'sci',scilimits = (-4,4),useOffset = True, useMathText = True)
		plt.ticklabel_format(axis = 'y',style = 'sci',scilimits = (-4,4),useOffset = True, useMathText = True)
		plt.ylabel('MSD (m^2)',fontsize = 16)
		plt.xlabel('Time (s)',fontsize = 16)
		plt.title('Mean Square Displacement of {} at {} K'.format(symbol,i))
		plt.savefig(path[0] + 'msd\\' + 'msd{}{}.png'.format(k,i))	
		plt.clf()
	#escrevendo os coeficientes de difusao"
		dif = open(path[0] + 'msd\\' + 'dif{}.txt'.format(k),'a')
		dif.write('{}  {}'.format(i,(m/6)*10**9))
		dif.write('\n')
		dif.close()  
print('ALL DONE')
	
