import pygame

def control(scale, posX, posY, angleX, angleY, midlePress, running = True):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				scale *= 1.05
			elif event.button == 5:
				scale /= 1.05
			elif event.button == 2:
				midlePress = True
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
			midlePress = False

	mx, my = pygame.mouse.get_rel()
	if midlePress:
		if pygame.key.get_pressed()[pygame.K_LSHIFT]:
			posX += mx
			posY += my
		else:
			angleY -= mx * 0.004
			angleX += my * 0.004

	return scale, posX, posY, angleX, angleY, midlePress, running		
