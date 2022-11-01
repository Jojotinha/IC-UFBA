file = open('')
for lines in file:
	lines = lines.strip()
	if lines.startswith('T'):
		lines = lines.split()
		x = lines[lines.index('index')+1:]
