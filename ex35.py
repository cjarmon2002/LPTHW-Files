from sys import exit

def gold_room():
	print "This room is full of gold coins. How many do you take?"

	choice = raw_input("> ")
	if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if "honey" in choice:
			dead("The bear looks at you then slaps your face off.")
		elif "taunt" in choice and not bear_moved:
			print "The bear has moved from the door. you can go through it now."
			bear_moved = True
		elif "taunt" in choice and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif "door" in choice and not bear_moved:
			print "There is a bear in the way!"
		elif "door" in choice and bear_moved:
			gold_room()
		else:
			print "I have no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	print why, "Good job, you're dead!"
	exit(0)

def start():
	print "You are in a dark room."
	print "there is a door to your right and left."
	print "Whice one do you take?"

	choice = raw_input("> ")

	if "left" in choice:
		bear_room()
	elif "right" in choice:
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()