#!/usr/bin/python
c = 0
# + or - or / or *
cmplist = []
mylist = []
def search(arg_list, x, y):
	global c
	c += 1
	if x < 0 or y < 0 or x > len(arg_list[0]) or y > len(arg_list):
		print "nil:" + str(c) + ":" + "x = " + str(x) + ": " + "y = " + str(y) + "\n"
		return 1
	search(arg_list, x, y-1)
	search(arg_list, x+1, y)
	search(arg_list, x, y+1)
	search(arg_list, x-1, y)

for line in open('data.txt', 'r'):
	line = line.rstrip()
	mylist.append(line)
	#initialize output list
	cmplist.append(' ' * len(line))

# input
for x in mylist :      
	print x;

# output
for x in cmplist :      
	print x;

#search(mylist, 0, 0)

