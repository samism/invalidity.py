# Invalidity.py
___

This program tests for the invalidity of an argument using an algorithm centered around the [shortened truth table method](http://ocw.mit.edu/courses/linguistics-and-philosophy/24-241-logic-i-fall-2005/readings/chp08.pdf) in [predicate logic](http://en.wikipedia.org/wiki/Predicate_logic).

The algorithm's objective is to **find an instance in which all the premises of an 
argument can be found true while having the conclusion false in a universe of one member**.

If the algorithm cannot find this case in a universe of one member, it will append members to the universe until it reaches a point in which the amount of members allows for this case to occur. Many arguments will never arrive at this case because they are (likely) valid.

If this instance is found (it could take a while), the program will terminate and report how many members a universe needs to contain for the invalid case to occur as well as which premises must be true and which false.

It will terminate at the first finding of such a case because if an argument is invalid in one universe, it is invalid in all universes. 

Due to computional limitations of most computers, the upper-bound for the amount of members
appendable to the universe will quickly become limited.

## Format for a statement

((E)x)[A-Z]x[A-Z]x


## Premise and Conclusion elements

| Quantifier scope		| Symbol	| Connective for the statement |	
| ----------------------|:---------:|-----------------------------:|
| Universal				|	(x)		|	**&sup;**				   |
| Existential			|	(Ex)	|	**&sdot;**                 |


## Misc. Rules

*Predicates are capital letters A-Z

*Constants are small letters a-w