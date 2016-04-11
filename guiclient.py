import pygame, sys, socket
from pygame.locals import *
#from drawing import *

port = int(raw_input("define port: "))
#host = raw_input("define host: ")
conn = socket.socket()
host = socket.gethostname()
conn.connect((host,port))

pygame.init()

windowSurface = pygame.display.set_mode((300,500), 0, 32)
pygame.display.set_caption('Hello World')

BLK = (0, 0, 0)
BKGD = (0, 128, 255)

INVALID = "Invalid move!"

Ximg = pygame.image.load('X.png')
XSimg = pygame.transform.scale(Ximg, (64, 64))
Oimg = pygame.image.load('O.png')
OSimg = pygame.transform.scale(Oimg, (64, 64))

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

def drawLetter(letter, pos):
	let = pygame.Rect(pos, (64, 64))
	if letter == 'X':
		windowSurface.blit(XSimg, X)
	else:
		windowSurface.blit(OSimg, O)

windowSurface.fill(BKGD)
drawBoard()
turnX = True

while True:
	for event in  pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			#conn.send("Update")
			ms = event.pos
			boardClick = True
			willDraw = True
			
			if turnX:
				letter = 'X'
			else:
				letter = 'O'

			if ms[0]>0 and ms[0]<100 and ms[1]>0 and ms[1]<100:
				drawpos = (18,18)
				xpos = '0'
				ypos = '0'
				#conn.send(letter + '0' + '0')
			elif ms[0]>100 and ms[0]<200 and ms[1]>0 and ms[1]<100:
				drawpos = (118,18)
				xpos = '1'
				ypos = '0'
				#conn.send(letter + '1' + '0')
			elif ms[0]>200 and ms[0]<300 and ms[1]>0 and ms[1]<100:
				drawpos = (218,18)
				xpos = '2'
				ypos = '0'
				#conn.send(letter + '2' + '0')
			elif ms[0]>0 and ms[0]<100 and ms[1]>100 and ms[1]<200:
				drawpos = (18,118)
				xpos = '0'
				ypos = '1'
				#conn.send(letter + '0' + '1')
			elif ms[0]>100 and ms[0]<200 and ms[1]>100 and ms[1]<200:
				drawpos = (118,118)
				xpos = '1'
				ypos = '1'
				#conn.send(letter + '1' + '1')
			elif ms[0]>200 and ms[0]<300 and ms[1]>100 and ms[1]<200:
				drawpos = (218,118)
				xpos = '2'
				ypos = '1'
				#conn.send(letter + '2' + '1')
			elif ms[0]>0 and ms[0]<100 and ms[1]>200 and ms[1]<300:
				drawpos = (18,218)
				xpos = '0'
				ypos = '2'
				#conn.send(letter + '0' + '2')
			elif ms[0]>100 and ms[0]<200 and ms[1]>200 and ms[1]<300:
				drawpos = (118,218)
				xpos = '1'
				ypos = '2'
				#conn.send(letter + '1' + '2')
			elif ms[0]>200 and ms[0]<300 and ms[1]>200 and ms[1]<300:
				drawpos = (218,218)
				xpos = '2'
				ypos = '2'
				#conn.send(letter + '2' + '2')
			else:
				boardClick = False
				print "not drawing or sending data"

			#if conn.recv(1024) == INVALID:
				#willDraw = False

			if boardClick:
				conn.send("U" + letter + xpos + ypos)
				boardmsg = conn.recv(1024) #info from server about update
				print boardmsg
				if boardmsg == "Invalid move!":
					willDraw = False
				if willDraw:
					if turnX:
						drawX(drawpos)
					else:
						drawO(drawpos)
					turnX = not turnX

		if event.type == KEYDOWN:
			print event.key
			if event.key == ord('r'):
				conn.send("R")
				windowSurface.fill(BKGD)
				drawBoard()
			elif event.key == ord('p'):
				conn.send("P")
				print conn.recv(1024) #text version of board

	pygame.display.update()
