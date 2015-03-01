#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import datetime
import urllib2

arg = sys.argv
arglen = len(sys.argv)

if (arglen==1):
	print ""
	print "example:"
	print ""
	print "  $ prigiza ASINCODE1 ASINCODE2 ASINLIST.txt ASINCODE3 ASINLIST2.txt"
	print ""
	print "Problem? Please visit http://hslab.org/"
	print ""
	exit()




def getrise(asin):
	dlurl = 'http://so-bank.jp/detail/?code='+asin

	tmp = urllib2.urlopen( dlurl )
	html = tmp.readlines(); tmp.close()

	x = 2 ; y = ""
	z = 2 ; w = ""

	for tmp in html:
		if ( tmp.find("new Date") >= 0 ):
			x = x - 1
			if (x<0): y = y + tmp

		if ( tmp.find("<span class=\x22red\x22><strong>") >= 0 ):
			z = z - 1
			if (z==0): w = tmp

	y = y.replace(')','')
	y = y.replace('[new Date(','')
	y = y.replace(']','')
	y = y.replace('				','')
	y = y.split(",")
	y = map(int, y)

	w = w.replace('\t\t\t\t\t\t\t\t<span class="red"><strong>\xc2\xa5 ','')
	w = w.replace('</strong></span></li>\n','')
#	w = str(w)
	if ( w.isdigit() == False ) : w = 0

	rankold = 0 ; rise = 0
	for i in range( 0 , len(y), 4):
		today = datetime.date.today()
		scanning = datetime.date( y[i], y[i+1]+ 1, y[i+2] )
		tmp = today - scanning
#		print y[i], y[i+1]+1, y[i+2], y[i+3], tmp.days

		if ( rankold < y[i+3] ) : rise = rise + 1
		rankold = y[i+3]

		if ( tmp.days > 29 ) : break

	return rise,w


for i in range(1, arglen):
	tmp = os.path.isfile(arg[i])

	if ( '.' in arg[i]):
		if ( tmp == False):
			print "!! ERROR !!  "+arg[i]+": file not found."
			exit()

		if ( tmp == True ):
			tmp = ""
			f = open(arg[i])

			if( i == 1 ):
				asinlist = f.read()
			else:
				asinlist += "\n"+f.read()

			f.close()
			continue

	if( i == 1 ):
		asinlist = arg[i]
	else:
		asinlist += "\n"+arg[i]

for i in asinlist.split('\n'):
	tmp = getrise(i)

	if (tmp>=5):
		print str(tmp[0])+","+str(tmp[1])+","+str(i)
