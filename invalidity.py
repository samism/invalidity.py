import sys
import os

class Invalidity(object):
	# computes which variables must be T or F to arrive at an invalid case (1 universe, first)
	def invalidCase(self, statements):
		return 'foo-bar'

	# instantiates quantified statement for a given member of the universe
	def instantiateStatement(self, statement, member):
		i_statement = ''
		pred = statement[statement.find(')') + 1:len(statement)].split('x') # list of predicates
		pred = pred[:-1] # don't need first arg (filename)
		#print 'Predicates from statement: ' + str(pred)

		for i in pred:
			i_statement += i + member
			if statement.startswith('(x)') and pred[0] == i:
				i_statement += '.'
			elif statement.startswith('(Ex)') and pred[0] == i:
				i_statement += 'v'

		return i_statement

	def __init__(self, args):
		args = args[1:] # get rid of 1st arg which is the script name

		self.members = ['a'] # universe begins with a single member - a
		self.statements = list() # format for a valid premise/conclusion -> ((E)x)A-ZxA-Zx

		if len(args) < 1 or len(args) > 3:
			print 'Usage: python invalidity.py "[premise]" "[premise]" "[conclusion]"'
			print 'where premise/conc formatted: ((E)x)A-ZxA-Zx'
			exit(1)

		# obtain instantiated forms of the given statements
		for i in args:
			for j in self.members:
				self.statements.append(self.instantiateStatement(i, j))

		#...
		print self.invalidCase(self.statements)

Invalidity(sys.argv)