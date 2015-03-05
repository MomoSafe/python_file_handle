
#coding:utf8
a=raw_input("please enter file name:  ")
for i in set( x for x in open( str(a) ).read( ).replace( '\n' ,' ' ).split(' ') if x ):
	print(i)