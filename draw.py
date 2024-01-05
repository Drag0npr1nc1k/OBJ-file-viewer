import pygame
from math import cos, sin
from settings import *



def drawModel(screen, scale, positionX, positionY, angleX, angleY, vertices, edges, planes):
	if drawPlane:
		for plane in planes:
			points = []
			for idx in plane:
				vx, vy, vz = vertices[idx]

				tempY = vy * cos(angleX) - vz * sin(angleX)
				tempZ = vy * sin(angleX) + vz * cos(angleX)
				tempX = vx * cos(angleY) - tempZ * sin(angleY)

				x, y = int(positionX + scale * tempX), int(positionY - scale * tempY)
				points.append((x, y))
			
			pygame.draw.polygon(screen, (161, 161, 161), points)


	for edge in edges:
		v1 = vertices[edge[0]]
		v2 = vertices[edge[1]]

		v1x, v1y, v1z = v1
		v2x, v2y, v2z = v2

		tempY1 = v1y * cos(angleX) - v1z * sin(angleX)
		tempZ1 = v1y * sin(angleX) + v1z * cos(angleX)
		tempX1 = v1x * cos(angleY) - tempZ1 * sin(angleY)

		tempY2 = v2y * cos(angleX) - v2z * sin(angleX)
		tempZ2 = v2y * sin(angleX) + v2z * cos(angleX)
		tempX2 = v2x * cos(angleY) - tempZ2 * sin(angleY)

		x1, y1 = int(positionX + scale * tempX1), int(positionY - scale * tempY1)
		x2, y2 = int(positionX + scale * tempX2), int(positionY - scale * tempY2)

		pygame.draw.line(screen, (255, 140, 0), (x1, y1), (x2, y2))
		pygame.draw.circle(screen, (0, 0, 0), (x2, y2), 3)
