#!/usr/bin/python
# + or - or / or *
cmplist = []
mylist = []
colorlist = []
poslist = []

def getColor(arg_cmplist, arg_poslist):
	print poslist;
	return '*'

def search(arg_list, y, x, arg_color):

	for tmp in cmplist :      
		print tmp

	print "------------------------"
	cmplist[y][x] = arg_color
	poslist.append([x,y])
	if y > 0 and cmplist[y-1][x] == ' ' and arg_list[y][x] == arg_list[y-1][x]:
		search(arg_list, y-1, x, arg_color)
	if x+1 < len(arg_list[0]) and cmplist[y][x+1] == ' ' and arg_list[y][x] == arg_list[y][x+1]:
		search(arg_list, y, x+1, arg_color)
	if y+1 < len(arg_list) and cmplist[y+1][x] == ' ' and arg_list[y][x] == arg_list[y+1][x]:
		search(arg_list, y+1, x, arg_color)
	if x > 0 and cmplist[y][x-1] == ' ' and arg_list[y][x] == arg_list[y][x-1]:
		search(arg_list, y, x-1, arg_color)

for line in open('data.txt', 'r'):
	line = line.rstrip()
	mylist.append(str(line))
	#initialize output list
	cmplist.append(map(str, str(' ' * len(line))))

for line in open('color.txt', 'r'):
	line = line.rstrip()
	colorlist.append(str(line))

# input
for x in mylist :      
	print x;

# for y in range(0, len(mylist)):
# 	for x in range(0, len(mylist[0])):
# 		if cmplist[y][x] == ' ':
# 			posList = search(mylist, y, x, '*')	
#			myColor = getColor(cmplist, posList)
#			setColor(posList, myColor)

search(mylist, 3, 3, '@')
# output
for x in cmplist :      
	print x;

myColor = getColor(cmplist, poslist)
print myColor
#print checkChar(colorlist, 0, 0)


