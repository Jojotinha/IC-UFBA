import matplotlib.pyplot as plt
import numpy as np
T = [50.2 ,278.2  ,283.2  ,288.2  ,293.2  ,298.2 ,308.2, 318.15,333.15,500] #temperaturas das runs 

for i in T:
	x = list()
	y = list()
	file = 'wpress{}.dat'.format(i) 
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
	plt.savefig('wpress{}.png'.format(i))
	plt.clf()
	f = open('Press.txt','a')
        f.write('{} / {} +- {}'.format(i,np.mean(y),np.std(y)))
        f.write('\n')
f.close()
print('ALL DONE')
	
