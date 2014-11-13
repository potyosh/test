#!/usr/bin/python
# + or - or / or *
cmplist = []
mylist = []
colorlist = []
poslist = []

def setColor(arg_poslist, arg_color):
	print arg_poslist
	print arg_color

def getAvailableColor(arg_colorlist, arg_poslist):
	print "------------------------"
	usedColor = []
	for pos in arg_poslist:
		#above
		if pos[0]-1 > 0 and cmplist[pos[0]-1][pos[1]] != '@':
			if arg_colorlist[pos[0]-1][pos[1]] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]-1][pos[1]])
		#right
		if pos[1]+1 < len(arg_colorlist[0]) and cmplist[pos[0]][pos[1]+1] != '@':
			if arg_colorlist[pos[0]][pos[1]+1] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]][pos[1]+1])
		#bottom
		if pos[0]+1 < len(arg_colorlist) and cmplist[pos[0]+1][pos[1]] != '@':
			if arg_colorlist[pos[0]+1][pos[1]] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]+1][pos[1]])
		#left
		if pos[1]-1 > 0 and cmplist[pos[0]][pos[1]-1] != '@':
			if arg_colorlist[pos[0]][pos[1]-1] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]][pos[1]-1])

	if '+' not in usedColor:
		answer = '+'
	elif '-' not in usedColor:
		answer = '-'
	elif '/' not in usedColor:
		answer = '/'
	elif '*' not in usedColor:
		answer = '*'

	return answer

def search(arg_list, y, x, arg_color):

	for tmp in cmplist :      
		print tmp

	print "------------------------"
	cmplist[y][x] = arg_color
	poslist.append([y,x])
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
	colorlist.append(map(str, str(line)))

# input
for x in mylist :      
	print x;

# for y in range(0, len(mylist)):
# 	for x in range(0, len(mylist[0])):
# 		if cmplist[y][x] == ' ':
# 			posList = search(mylist, y, x, '*')	
#			myColor = getColor(cmplist, posList)
#			setColor(posList, myColor)

search(mylist, 2, 5, '@')
# output
for x in cmplist :      
	print x;

myColor = getAvailableColor(colorlist, poslist)
setColor(poslist, myColor)
#print myColor
#print checkChar(colorlist, 0, 0)


