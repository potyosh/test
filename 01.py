#!/usr/bin/python
#c = 0
# + or - or / or *
cmplist = []
mylist = []
color = '*'

def search(arg_list, y, x):
	#global c
	#global cmplist
	#c += 1
	
	#print y
	#print x
	#if x < 0 or y < 0 or y >= len(arg_list) or x >= len(arg_list[0]) or cmplist[y][x] != ' ' or c > 30 :
	#	print "nil:" + str(c) + ":" + "y = " + str(y) + ": " + "x = " + str(x)
	#	return 1

	for tmp in cmplist :      
		print tmp

	#print "hoge" + str(cmplist[y][x]) + "aaa"
	print "------------------------"
	cmplist[y][x] = color
	if y > 0 and cmplist[y-1][x] == ' ' and arg_list[y][x] == arg_list[y-1][x]:
		search(arg_list, y-1, x)
	if x+1 < len(arg_list[0]) and cmplist[y][x+1] == ' ' and arg_list[y][x] == arg_list[y][x+1]:
		search(arg_list, y, x+1)
	if y+1 < len(arg_list) and cmplist[y+1][x] == ' ' and arg_list[y][x] == arg_list[y+1][x]:
		search(arg_list, y+1, x)
	if x > 0 and cmplist[y][x-1] == ' ' and arg_list[y][x] == arg_list[y][x-1]:
		search(arg_list, y, x-1)

for line in open('data.txt', 'r'):
	line = line.rstrip()
	mylist.append(str(line))
	#initialize output list
	cmplist.append(map(str, str(' ' * len(line))))

# input
for x in mylist :      
	print x;

search(mylist, 0, 0)
color = '-'
search(mylist, 0, 1)
color = '/'
search(mylist, 0, 2)
color = '-'
search(mylist, 0, 5)
color = '/'
search(mylist, 0, 9)
color = '/'
search(mylist, 3, 0)
color = '+'
search(mylist, 3, 2)
# output
for x in cmplist :      
	print x;



