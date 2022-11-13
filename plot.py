#Script para tratamento de dados gerados via LAMMPS 
#Leitura do arquivo info.txt
info = open(info.txt)
T = []
for line in info:
		if line.startswith('T'):
				T = (line[2:]).split()
		elif line.startswith('Source'):
			path = (line.strip())[7:]
print(T)
print(path)

				
				
				
