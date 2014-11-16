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
		if pos[0]-1 >= 0 and arg_colorlist[pos[0]-1][pos[1]] != '@':
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
		if pos[1]-1 >= 0 and arg_colorlist[pos[0]][pos[1]-1] != '@':
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

	return ansColList

def search(arg_list, y, x, arg_color):
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

def colorTrace(arg_allposlist, arg_posIndex, arg_collist, arg_colIndex, arg_cmplist):
	print "~~~posindex="+str(arg_posIndex)+", colindex="+str(arg_colIndex)
	
	for line in arg_cmplist:
		print line
	if arg_posIndex >= len(arg_allposlist):
		return

	print "color hist"
	colHist.append(arg_collist)
	for x in colHist :      
		print x;

	if arg_collist:
		print "nuru," + arg_collist[arg_colIndex]
		setColor(arg_allposlist[arg_posIndex], arg_collist[arg_colIndex], arg_cmplist)
		arg_posIndex += 1
		setColor(arg_allposlist[arg_posIndex], '@', arg_cmplist)
		arg_collist = getAvailableColor(arg_cmplist, arg_allposlist[arg_posIndex])
		if arg_posIndex < len(arg_allposlist):
			colorTrace(arg_allposlist, arg_posIndex, arg_collist, 0, arg_cmplist)
		if arg_colIndex + 1 < len(arg_collist):
			colorTrace(arg_allposlist, arg_posIndex, arg_collist, arg_colIndex+1, arg_cmplist)

		print "hoge" + str(arg_collist)


	# if arg_collist and arg_posIndex+1 < len(arg_allposlist):
	# 	setColor(arg_allposlist[arg_posIndex], arg_collist[arg_colIndex], arg_cmplist)
	# 	if arg_posIndex+1 < len(arg_allposlist) and arg_colIndex < len(arg_collist):
	# 		collist = getAvailableColor(arg_cmplist, arg_allposlist[arg_posIndex+1])
	# 		colHist.append(collist)
	# 		colorTrace(arg_allposlist, arg_posIndex+1, collist, arg_colIndex, arg_cmplist)
	# else:
	# 	return
		#setColor(arg_allposlist[arg_posIndex-1], '@', arg_cmplist)
		#colorTrace(arg_allposlist, arg_posIndex-1, collist, arg_colIndex+1, arg_cmplist)

# input
inputlist = []
# output
cmplist = []
# position list
poslist = []
# position list list
allposlist = []
# color list
collist = []
# color hitstory
colHist = []
# color apply list
colApplyList = []

for line in open('data.txt', 'r'):
	line = line.rstrip()
	inputlist.append(str(line))
	#initialize output list
	cmplist.append(map(str, str(' ' * len(line))))

for x in inputlist :      
	print x;

for y in range(0, len(inputlist)):
	for x in range(0, len(inputlist[0])):
		if cmplist[y][x] == ' ':
			poslist = []
			search(inputlist, y, x, '@')	
			allposlist.append(poslist)

# Re-initialize output
cmplist = []
for line in inputlist:
	#initialize output list
	cmplist.append(map(str, str(' ' * len(line))))

for line in cmplist:
	print line

# Position block list complete
print "~~~~~~~~~~Position Block List~~~~~~~~~~~"
for x in allposlist :
 	print x;

collist = getAvailableColor(cmplist, allposlist[0])
colorTrace(allposlist, 0, collist, 0, cmplist)

print "~~~~~~~~~~Color Hitstory List~~~~~~~~~~~"
for x in colHist :      
	print x;

print "~~~~~~~~~~Answer~~~~~~~~~~~"
# output
for x in cmplist :      
	print x;

