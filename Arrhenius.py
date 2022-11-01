# Arhennius Plot 
#João Victor Lemos Valle
#=====================================================
import matplotlib.pyplot as plt
import numpy as np
import math
file = ('dif_temp.txt')
fhand = open(file)
x = []
y = []
for line in fhand:
	line = line.split()
	x.append(1/float(line[0]))
	y.append(math.log(float(line[1])*10**-9,10)+9)
x = np.array(x)
y = np.array(y)
m,b = np.polyfit(x,y,1)
mn = np.min(x)
mx = np.max(x)
x0 = np.linspace(mn,mx,1000)
y0 = m*x0 + b
plt.plot(x,y,'r+',markersize = 8)
plt.plot(x0,y0,linewidth = 1, color = 'black')
plt.xlabel('1/T (K)')
plt.ylabel('9+log D (m^2/s)')
plt.savefig('Arrhenius-Plot.png')
f = open('Energy.txt','w')
f.write('Activation Energy: {} kcal/mol'.format(m)) 
f.close()
print('THE CODE WORKS, WELL DONE!!!')
