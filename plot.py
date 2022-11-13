#Script para tratamento de dados gerados via LAMMPS 
#========================================================================
#========================================================================

import matplotlib.pyplot as plt
import numpy as np

#========================================================================
#Leitura do arquivo info.txt
#========================================================================
info = open('info.txt')
for line in info:
	if line.startswith('T'):
		T = (line.split())[2:]
	elif line.startswith('Source'):
		path = (line.split())[2:]
print(T)
print(path)

#========================================================================
#Energia Potencial
#========================================================================


for i in T:
	x = list()
	y = list()
	file = path[0] + 'termo\\energies\\' + 'wpe{}.dat'.format(i) 
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
	plt.ylabel('Potential Energy (kcal/mol)',fontsize = 10)
	plt.xlabel('Time (fs)',fontsize = 10)
	plt.title('Potential energy versus Time at {} K'.format(i))
	plt.savefig(path[0]+'termo\\energies\\'+'wpe{}.png'.format(i))
	plt.clf()
	f = open(path[0] + 'termo\\energies\\' + 'PE.txt','a')
        f.write('{} / {} +- {} ({})'.format(i,np.mean(y),round(np.std(y),3),np.std(y)*100/np.mean(y)))
        f.write('\n')
f.close()

#========================================================================
#Energia Cinética
#========================================================================
x = []
y = []
for i in T
	file = path[0] + 'termo\\energies\\' + 'wke{}.dat'.format(i) 
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
	plt.ylabel('Kinetical Energy (kcal/mol)',fontsize = 10)
	plt.xlabel('Time (fs)',fontsize = 10)
	plt.title('Kinetical energy versus Time at {} K'.format(i))
	plt.savefig(path[0] + 'termo\\energies\\' + 'wke{}.png'.format(i))
	plt.clf()
	f = open(path[0] + 'termo\\energies\\' + 'KE.txt','a')
	f.write('{} / {} +- {}'.format(i,np.mean(y),round(np.std(y),3))
	f.write('\n')
f.close()

#========================================================================
#Temperatura
#========================================================================
x = []
y = []
for i in T:

	file = path[0] + 'termo\\temperatures\\' + 'wtemp{}.dat'.format(i) 
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
	plt.savefig(path[0] + 'termo\\temperatures\\' + 'wtemp{}.png'.format(i))
	plt.clf()
	f = open(path[0] + 'termo\\temperatures\\' + 'Temp.txt','a')
	f.write('{} / {} +- {}'.format(i,np.mean(y),round(np.std(y),3)))
	f.write('\n')
f.close()

#========================================================================
#Pressão
#========================================================================
x = []
y = []
for i in T:
	x = list()
	y = list()
	file = path[0] + 'termo\\pressures\\' + 'wpress{}.dat'.format(i) 
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
	plt.ylabel('Pressure (atm)',fontsize = 16)
	plt.xlabel('Time (fs)',fontsize = 16)
	plt.title('Pressure versus Time at {} K'.format(i))
	plt.savefig(path[0] + 'termo\\pressures\\' + 'wpress{}.png'.format(i))
	plt.clf()
	f = open(path[0] + 'termo\\pressures\\' + 'Press.txt','a')
        f.write('{} / {} +- {}'.format(i,np.mean(y),round(np.std(y),3)))
        f.write('\n')
f.close()
#========================================================================
#Densidade
#========================================================================
		
for i in T:
x = []
y = []
for i in T:
	x = list()
	y = list()
	file = path[0] + 'termo\\densities\\' + 'wrho{}.dat'.format(i) 
	fhand = open(file) #abrindo o arquivo correspondente a temperatura i 
# extraindo o x e o y 
	for line in fhand:
		line = line.split()
		try:
			float(line[0])
		except:
			continue
		x.append(float(line[0]))
		y.append(float(line[1])*)
#criando o grafico
	plt.plot(x,y,linewidth = 1,color = 'black')
	plt.ticklabel_format(axis = 'x',style = 'sci',scilimits = (-4,4),useOffset = True, useMathText = True)
	plt.ylabel('Density (g/cm^3)',fontsize = 16)
	plt.xlabel('Time (fs)',fontsize = 16)
	plt.title('Density versus Time at {} K'.format(i))
	plt.savefig(path[0] + 'termo\\densitites\\' + 'wrho{}.png'.format(i))
	plt.clf()
	f = open(path[0] + 'termo\\densities\\' + 'Rho.txt','a')
        f.write('{} / {} +- {}'.format(i,np.mean(y),round(np.std(y),3)))
        f.write('\n')
f.close()
		
print('ALL DONE!!!!')

