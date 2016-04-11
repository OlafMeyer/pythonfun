#!/usr/bin/python

import socket
from Tkinter import *

class player:
	def __init__(self, n):
		self.name = n

port = int(raw_input("define port: "))

conn = socket.socket()
host = socket.gethostname()
#port = 12345

conn.connect((host,port))

while True:
	print "***MENU***"
	print "1 - Enter names"
	print "2 - Get names"
	print "3 - Show Board"
	print "4 - Make move"
	print "0 - Exit"
	choice = int(raw_input("> "))

	if choice == 1:
		p1name = raw_input("What is player one's name: ")
		p1 = player(p1name)
		p2name = raw_input("What is player two's name: ")
		p2 = player(p2name)
	elif choice == 2:
		print "Player one's name is " + p1.name + " and player two's name is " + p2.name
	elif choice == 3:
		conn.send("Print")
		print conn.recv(1024)
	elif choice == 4:
		conn.send("Update")
		letter = raw_input("Send which letter?")
		x = raw_input("To which X coord?")
		y = raw_input("To which Y coord?")
		conn.send(letter + x + y)
		print conn.recv(1024) #success or fail message
	elif choice == 0:
		break

print "Thanks for playing!"

conn.close