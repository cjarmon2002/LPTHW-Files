i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i  += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num


def counter(top):
	i = 0
	numbers = []

	while i < top:
		print "i is %d" % i
		numbers.append(i)

		i += 1
		print "Numbers is: ", numbers

	print "The numbers: "

	for num in numbers:
		print num

top = int(raw_input("> "))

counter(top)