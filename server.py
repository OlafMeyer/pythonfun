#!/usr/bin/python

class game:
	board = [['.' for x in range(3)] for x in range(3)]
	def update(self, letter, x, y):
		self.board[x][y] = letter
		return
	def printer(self):
		p = "  0   1   2\n0 " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + "\n -----------\n1 " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + "\n -----------\n2 " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2]
		return p
	def clear(self):
		self.board = [['' for x in range(3)] for x in range(3)]
		return

import socket

port = int(raw_input("define port: "))

game = game()
sock = socket.socket()
host = socket.gethostname()
#port = 12345
sock.bind((host, port))
#print game.printer()

sock.listen(5)
c, addr = sock.accept()
print 'Got connection from', addr
while True:
	#printout = game.printer
	choice = c.recv(1024)
	if choice == "Print":
		c.send(game.printer())
	elif choice == "Update":
		print "got update"
		u = c.recv(1024)
		print u
		letter = u[0]
		x = int(u[1])
		y = int(u[2])
		if x > -1 and x < 3 and y > -1 and y < 3 and game.board[x][y] == ".":
			game.update(letter, x, y)
			c.send(letter + " was placed at " + u[1] + "," + u[2])
		else:
			c.send("Invalid move!")
	
c.close()

#  0   1   2
#0   |   |
# -----------
#1   |   |   
# -----------
#2   |   |   