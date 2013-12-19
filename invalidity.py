import sys
import os

class Invalidity(object):

	# instantiates quantified statement for a given member of the universe

	def instantiateStatement(self, statement, member):
		i_statement = None
		pred = statement[statement.find(')') + 1:len(statement)].split('x') # list of predicates
		pred = pred[:-1]
		print 'Predicates from statement: ' + str(pred) + ', length: ' + str(len(pred))

		#find a way to shorten this later. 
		#too much code just to choose '.' or 'v'
		for i in range(len(pred)):
			if statement.startswith('(x)'):
				i_statement = pred[i] + member
				if i == 0:
					i_statement = i_statement + '.'
			elif statement.startswith('(Ex)'):
				i_statement = pred[i] + member
				if i == 0:
					i_statement = i_statement + 'v'

		return i_statement

	def __init__(self, args):
		args = args[1:] #get rid of 1st arg which is the script name

		self.members = ['a'] #universe begins with a single member - a
		self.statements = list() #format for a valid premise/conclusion -> ((E)x)A-ZxA-Zx

		if len(args) < 1 or len(args) > 3:
			print 'Usage: python invalidity.py "[premise]" "[premise]" "[conclusion]"'
			print 'where premise/conc formatted: ((E)x)A-ZxA-Zx'
			exit(1)

		#print 'Statements given: ' + str(args)

		for i in args:
			for j in self.members:
				self.statements.append(self.instantiateStatement(i, j))

		print str(self.statements)


Invalidity(sys.argv)