#!/usr/bin/python
# + or - or / or *

class AllPosColor:
	def __init__(self, arg_poslist, arg_availColList):
		self.poslist = []
		self.arg_availColList = []

def setColor(arg_poslist, arg_color, arg_cmplist):
	for pos in arg_poslist:
		arg_cmplist[pos[0]][pos[1]] = arg_color

def getAvailableColor(arg_colorlist, arg_poslist):
	usedColor = []
	ansCol = '@'
	ansColList = []
	for pos in arg_poslist:
		#above
		if pos[0]-1 > 0 and arg_colorlist[pos[0]-1][pos[1]] != '@':
			if arg_colorlist[pos[0]-1][pos[1]] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]-1][pos[1]])
		#right
		if pos[1]+1 < len(arg_colorlist[0]) and arg_colorlist[pos[0]][pos[1]+1] != '@':
			if arg_colorlist[pos[0]][pos[1]+1] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]][pos[1]+1])
		#bottom
		if pos[0]+1 < len(arg_colorlist) and arg_colorlist[pos[0]+1][pos[1]] != '@':
			if arg_colorlist[pos[0]+1][pos[1]] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]+1][pos[1]])
		#left
		if pos[1]-1 > 0 and arg_colorlist[pos[0]][pos[1]-1] != '@':
			if arg_colorlist[pos[0]][pos[1]-1] not in usedColor:
				usedColor.append(arg_colorlist[pos[0]][pos[1]-1])

	if '+' not in usedColor:
		ansCol = '+'
	elif '-' not in usedColor:
		ansCol = '-'
	elif '/' not in usedColor:
		ansCol = '/'
	elif '*' not in usedColor:
		ansCol = '*'

	if '+' not in usedColor:
		ansColList.append('+')
	if '-' not in usedColor:
		ansColList.append('-')
	if '/' not in usedColor:
		ansColList.append('/')
	if '*' not in usedColor:
		ansColList.append('*')

	print "------------------------"
	print ansColList
	colHist.append(ansColList)
	return ansCol
	#return ansColList

def search(arg_list, y, x, arg_color):
	print "~~~~"
	for tmp in cmplist :      
		print tmp

	# print "------------------------"
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

# input
inputlist = []
# output
cmplist = []
# position list
poslist = []
# position list list
allposlist = []
# color hitstory
colHist =[]

for line in open('data.txt', 'r'):
	line = line.rstrip()
	inputlist.append(str(line))
	#initialize output list
	cmplist.append(map(str, str(' ' * len(line))))

# for line in open('color.txt', 'r'):
# 	line = line.rstrip()
# 	colorlist.append(map(str, str(line)))


for x in inputlist :      
	print x;

for y in range(0, len(inputlist)):
	for x in range(0, len(inputlist[0])):
		if cmplist[y][x] == ' ':
			poslist = []
			search(inputlist, y, x, '@')	
			allposlist.append(poslist)
			myColor = getAvailableColor(cmplist, poslist)
			#if myColor == '@'
				# BackTrace!
			setColor(poslist, myColor, cmplist)
			#complete = checkComplete()

#search(mylist, 4, 7, '@')

#myColor = getAvailableColor(colorlist, poslist)
#setColor(poslist, myColor)

# output
for x in cmplist :      
	print x;

# output
for x in allposlist :      
	print x;

for x in colHist :      
	print x;

setColor(poslist, myColor, cmplist)

#print myColor
#print checkChar(colorlist, 0, 0)


