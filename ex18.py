# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()


# this is a personal test funcion
def test_monkey(arg1, arg2, arg3):
	print "I have three values"
	print "They are %r and %r." % (arg1, arg2)
	print "Oops that was only two, the third one is %r." % (arg3)


print "Give me three words"
x = raw_input("> ")
y = raw_input("> ")
z = raw_input("> ")

test_monkey(x,y,z)