import matplotlib.pyplot as plt
import numpy as np
try:
	file = open('spc.lammps') 
except:
	file = open('tip4p.lammps')
for lines in file:
	lines = lines.strip()
	if lines.startswith('T'):
		lines = lines.split()
		T = lines[lines.index('index')+1:] 

for i in T:
	x = list()
	y = list()
	file = 'wtemp{}.dat'.format(i) 
	fhand = open(file) #abrindo o arquivo correspondente a temperatura i 
# extraindo o x e o y 
	for line in fhand:
		line = line.split()
		try:
			float(line[0])
		except:
			continue
		x.append(float(line[0]))
		y.append(float(line[1]))
#criando o grafico
	plt.plot(x,y,linewidth = 1,color = 'black')
	plt.ticklabel_format(axis = 'x',style = 'sci',scilimits = (-4,4),useOffset = True, useMathText = True)
	plt.ylabel('Temperature (K)',fontsize = 16)
	plt.xlabel('Time (fs)',fontsize = 16)
	plt.title('Temperature variance over time at {}'.format(i))
	plt.savefig('wtemp{}.png'.format(i))
	plt.clf()
	f = open('Temp.txt','a')
        f.write('{} / {} +- {}'.format(i,np.mean(y),np.std(y)))
        f.write('\n')
f.close()
print('ALL DONE')
	
