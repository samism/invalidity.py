''' 
This program tests for the invalidity of an argument using 
an algorithm centered around the shortened truth table method in predicate logic.

The algorithm's objective is to find an instance in which all the premises of an 
argument can be found true while having the conclusion false in a universe of one member.

If the algorithm cannot find this case in a universe of one member, it will append members
to the universe until it reaches a universe in which the amount of members allows for this case
to occur. Many arguments will never arrive at this case because they are likely valid.

If this instance is found, the program will terminate and report how many members a universe
needs to contain for the invalid case to occur as well as which premises must be true and which false.

It will terminate at the first finding of such a case because if an argument is invalid in one universe,
it is invalid in all universes. 

Due to computional limitations of most computers, the upper-bound for the amount of members
appendable to the universe is 100.

Universally quantified statement 	- (x) -> implies horshoe
Existentially quantified statement 	- (Ex) -> implies dot

Predicates are capital letters A-Z
Constants are small letters a-w
'''

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





















