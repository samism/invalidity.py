import sys
import os

class Invalidity(object):

	# instantiates quantified statement for a given member of the universe

	def instantiatePremise(self, premise, member):
		i_premise = None
		pred = premise[premise.find(')') + 1:len(premise)].split('x') # list of predicates
		pred = pred[:-1]
		print 'Predicates from statement: ' + str(pred)

		for i in range(len(pred)):
			if premise.startswith('(x)'):
				i_premise = pred[i] + member
				if i != len(pred):
					i_premise = i_premise + '.'
			elif premise.startswith('(Ex)'):
				i_premise = pred[i] + member
				if i != len(pred):
					i_premise = i_premise + 'v'

		return i_premise

	def __init__(self, args):
		args = args[1:] #get rid of 1st arg which is the script name

		self.members = ['a'] #universe begins with a single member - a
		self.statements = list() #format for a valid premise/conclusion -> ((E)x)A-ZxA-Zx

		if len(args) < 1 or len(args) > 3:
			print 'Usage: python invalidity.py "[premise]" "[premise]" "[conclusion]"'
			print 'where premise/conc formatted: ((E)x)A-ZxA-Zx'
			exit(1)

		print 'Statements given: ' + str(args)

		for i in args:
			for j in self.members:
				self.statements.append(self.instantiatePremise(i, j))

		print str(self.statements)


Invalidity(sys.argv)





















