import pygame, sys
from pygame.locals import *

def drawBoard():
	pygame.draw.line(windowSurface, BLK, (0,100), (300,100))
	pygame.draw.line(windowSurface, BLK, (0,200), (300,200))
	pygame.draw.line(windowSurface, BLK, (0,300), (300,300))
	pygame.draw.line(windowSurface, BLK, (100,0), (100,300))
	pygame.draw.line(windowSurface, BLK, (200,0), (200,300))

def drawX(pos):
	X = pygame.Rect(pos, (64, 64))
	windowSurface.blit(XSimg, X)

def drawO(pos):
	O = pygame.Rect(pos, (64, 64))
	windowSurface.blit(OSimg, O)