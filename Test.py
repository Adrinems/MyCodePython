# -*- coding: utf8 -*-
"""
>>> show_score()
"0 0"

>>> add_point(1)

>>> show_score()
"15 0"

>>> add_point(2)

>>> show_score()
"15 15"

>>> add_point(1)

>>> show_score()
"30 15"

>>> add_point(1)


>>> show_score()
"40 15"


>>> add_point(1)


>>> show_score()
"SET Player 1"

"""
p1 =0
p2 =0
def add_point(player):
	global p1, p2
	if player == 1:
		if p1 == 0:
			p1 += 15
		elif p1 == 15:
			p1 +=15
		elif p1 == 30:
			p1 +=10
		elif p1 == 40:
			p1 +=1
	else:
		if p2 == 0:
			p2 += 15
		elif p2 == 15:
			p2 +=15
		elif p2 == 30:
			p2 +=10
		elif p2 == 40:
			p2 +=1

def show_score():
	global p1, p2

	if (p1== 40) and (p1==p2):
		print "DEUCE"
	elif p1> 40 and p2 >=40 and p1> p2:
		print "ADV {0}".format(p2)
	elif p2> 40 and p1 >=40 and p2> p1:
		print "{0} ADV".format(p1)
	elif p1> 40 and p1 > p2 and ((p1-p2) >=1) :
		print '"SET Player 1"'
	elif p2> 40 and p2 > p1 and ((p2-p1) >=1) :
		print '"SET Player 2"'
	else:
		print '"{0} {1}"'.format(p1,p2)
