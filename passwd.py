#!/usr/bin/python

fich=open('/etc/passwd','r')
lines=fich.readlines()
fich.close()
dicc={}

for line in lines[:-1]: #Dejo fuera la ultima linea porque split me deja un \n al final
	slot=line.split(':')
	dicc[slot[0]]=slot[-1][:-1]

print 'El usuario root utiliza la shell ' + dicc['root'] + '\n'
try:
	print 'El usuario imaginario utiliza la shell ' + dicc['imaginario'] + '\n'
except KeyError:
	print 'El usuario imaginario no existe\n'
print "En total hay " + str(len(lines)) + " usuarios"
