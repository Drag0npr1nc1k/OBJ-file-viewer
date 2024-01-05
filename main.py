import pygame
from control import *
from settings import *
from draw import *
from model import *
from settings import *

pygame.init()

def run():
	global scale, zoomSpeed
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	vertices, edges, planes = loadingModel(pathToFile)
	pressed_middle_button, clock, running = False, pygame.time.Clock(), True
	positionX, positionY, angleX, angleY = WIDTH // 2, HEIGHT // 2, 0, 0
	midlePress = False

	while running:
		pygame.display.set_caption(f"FPS: {clock.get_fps():.2f} OBJ file viewer | powered by: Drag0n")
		screen.fill((79, 79, 79))

		scale, positionX, positionY, angleX, angleY, midlePress, running = control(scale, positionX, positionY, angleX, angleY, midlePress)
		drawModel(screen, scale, positionX, positionY, angleX, angleY, vertices, edges, planes)

		pygame.display.flip()
		clock.tick(60)
		pygame.display.update()

