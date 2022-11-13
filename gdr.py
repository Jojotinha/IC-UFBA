import matplotlib.pyplot as plt

info = open('info.txt')
for line in info:
	if line.startswith('T'):
		T = (line.split())[2:]
	elif line.startswith('Source'):
		path = (line.split())[2:]
print(T)
print(path)

for i in T:
	x = list()
	y = list()
	file = path[0] + 'gdr\\chloride' + 'gdr-nacl{}.dat'.format(i) 
	fhand = open(file) #abrindo o arquivo correspondente a temperatura i 
# extraindo o x e o y 
	for line in fhand:
		line = line.split()
		try:
			float(line[0])
		except:
			continue
		if line.startswith('450000'):
			continue
		x.append(float(line[1]))
		y.append(float(line[2]))
#criando o grafico
	plt.plot(x,y,linewidth = 1,color = 'black')
	plt.ticklabel_format(axis = 'x',style = 'sci',scilimits = (-4,4),useOffset = True, useMathText = True)
	plt.ylabel('G(r) ',fontsize = 10)
	plt.xlabel('Distancy (A)',fontsize = 10)
	plt.title('G(r) at {} K'.format(i))
	plt.savefig(path[0]+'termo\\energies\\'+'gdr-nacl{}.png'.format(i))
	plt.clf()
