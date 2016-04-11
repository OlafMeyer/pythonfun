#!/user/bin/python

class player:
	def __init__(self, n):
		self.name = n


while True:
	print "***MENU***"
	print "1 - Enter names"
	print "2 - Get names"
	print "3 - Exit"
	choice = int(raw_input("> "))

	if choice == 1:
		p1name = raw_input("What is player one's name: ")
		p1 = player(p1name)
		p2name = raw_input("What is player two's name: ")
		p2 = player(p2name)
	elif choice == 2:
		print "Player one's name is " + p1.name + " and player two's name is " + p2.name
	elif choice == 3:
		break

print "Thanks for playing!"