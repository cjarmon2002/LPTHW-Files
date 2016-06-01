from sys import exit

sword = False
key = False
beast = True

def start(swrd, ky, bst):
	(sword, key, beast) = (swrd, ky, bst)
	print "You stand in front of a cave deep in a forest."
	print "You have come here searching for treasue"
	print "Where do you go?"

	while True:
		choice = raw_input("> ")
		if "cave" in choice:
			cave(sword, key, beast)
		elif "forest" in choice:
			forest()
		else:
			print "I don't understand that, try again."

def cave(swrd, ky, bst):
	(sword, key, beast) = (swrd, ky, bst)
	print "You enter the cave."
	print "As you walk down its dimly lit hallway you see a path that slopes down"
	print "You also see a large open room further down the hall."
	print "Where do you go?"

	while True:
		choice = raw_input("> ")
		if "path" in choice:
			dead("You slide into bottomless darkness.")
		elif "room" in choice:
			room(sword, key, beast)
		else:
			print "I don't understand that, try again."

def room(swrd, ky, bst):
	(sword, key, beast) = (swrd, ky, bst)
	print "You enter into the large room"
	print "There are two doors, one to your left and one to your right."
	print "The corners of the room are shrouded in darkness"
	print "What would you like to do?"

	while True:
		choice = raw_input("> ")
		if "left" in choice:
			left(sword, key, beast)
		elif "right" in choice and not sword and beast:
			dead("You stand unarmed before a beast, it lunges for you.")
		elif "right" in choice and sword:
			right(sword, key, beast)
		elif "search" and "room" in choice and not sword:
			print "You find a sword, now what?"
			sword = True
		elif "search" and "room" in choice and sword:
			print "There is nothing else, choose a door."
		else:
			print "I do not understand that, try again."


def left(swrd, ky, bst):
	(sword, key, beast) = (swrd, ky, bst)
	print "There is a locked chest in this room"
	print "What would you like to do?"
	
	while True:
		choice = raw_input("> ")
		if "chest" in choice and not key:
			print "It's locked, there must be a key somewhere."
		elif "chest" in choice and key:
			print "You open the chest and find the treasue! Good job, you won."
			exit(0)
		elif "room" or "back" in choice:
			print "you return to the room"
			room(sword, key, beast)
		else:
			print "I do not understand that, try again."

	

def right(swrd, ky, bst):
	(sword, key, beast) = (swrd, ky, bst)
	if beast == False:
		print "The beast lies on the floor, think you need that key now?"
		choice = raw_input("> ")
		if "yes" in choice:
			print "You take the key and return to the room."
			key = True
			room(sword, key, beast)
		if "no" in choice:
			dead("You are too dumb to live.")

	if beast == True:
		print "There is a huge beast, it lunges at you."
		print "Your instincts cause you to raise your sword"
		print "The beast falls upon it and then collapes to the floor"
		print "You notice a small key around the beasts neck. What do you do?"
		beast = False

	while True:
		choice = raw_input("> ")
		if "key" in choice:
			print "You take the key and return to the room."
			key = True
			room(sword, key, beast)
		elif "room" in choice:
			print "You return to the room empty handed."
			room(sword, key, beast)
		else:
			print "I do not understand that, try again."
	

def dead(why):
	print why, "Good job, you're dead."
	exit(0)


def forest():
	print "You are a coward and run from adventrue."
	print "May you die a slow and boring death."
	exit(0)

start(sword, key, beast)
