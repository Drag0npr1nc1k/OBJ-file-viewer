def loadingModel(pathToFile):
	vertices = []
	edges = []
	planes = []

	with open(pathToFile, 'r') as f:
		lines = f.readlines()

	for line in lines:
		if line.startswith('v '):
			parts = line.split()
			vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
		elif line.startswith('f '):
			parts = line.split()
			indices = [int(part.split('/')[0]) - 1 for part in parts[1:]]
			
			planes.append(indices)

			if len(indices) == 3:
				edges.append((indices[0], indices[1]))
				edges.append((indices[0], indices[2]))
				edges.append((indices[1], indices[2]))
			elif len(indices) == 4:
				edges.append((indices[0], indices[1]))
				edges.append((indices[1], indices[2]))
				edges.append((indices[2], indices[3]))
				edges.append((indices[3], indices[0]))

	return vertices, edges, planes
