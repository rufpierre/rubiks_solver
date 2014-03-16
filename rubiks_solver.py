#! /usr/bin/env python
# -*- coding: utf-8 -*-

from engine import *
from collections import Counter

help = """f,r,b,l,d,t for standard transformations
F,R,B,L,D,T for reverse transformations
z to reset the cube
q to quit
"""

# clean screen
print("\033c")

# init the display
print(help)
print_cube(cube)

# choose between CLI mode or static mode
cli = True


#==============================================================================
# en cours:
# essayer de comprendre les genes et les organismes
# bidouiller l exemple que jai recopié dans le repertoire (le duppliquer)
# 	pour l amener vers un gene string au lieu de float
# 
# en cours 2
#     ai fait une seule classe de gene (pas d heritage)
#     il faut minimiser la fonction de fitness (donc l inverser)
#     bien comprendre comment marche le truc avec les floats
#==============================================================================

# fitness of the cube
def variance(x):
	"""variance = 1/(n-1) * sum(1,n,(x-m)²)"""
	m = float(sum(x))/len(x)
	return sum([(e-m)**2 for e in x])/(len(x)-1)

def dist(x):
	"""distribution of a list of values"""
	c = Counter(x)
	return [c[e] for e in sorted(c)]

def dist2(x):
	"""distribution of the colors on a cube facet"""
	return [x.count(e) for e in range(6)]

def fitness(cube):
	"""fitness of the cube is the sum of the variances for each facet of the cube
	max score multiplied by -1.
     cube in its initial state is -81 wich is the lowest and best score
     'cube in a cube' is -33"""
	return -sum([variance(dist2(cube[facet])) for facet in range(6)])


# static mode
if (not cli):
	rand_inst = "flfTrtffllTLbDBllt"
	pons_asinorum = "F2 B2 R2 L2 U2 D2"
	cube_in_a_cube = "F L F U' R U F2 L2 U' L' B D' B' L2 U"
	cube = chain(cube_in_a_cube, cube)
	print_cube(cube)
	print(fitness(cube))

# CLI mode
while cli:
	raw_in = raw_input()
	# quit
	if raw_in == 'q':
		# clean screen
		print("\033c")
		# exit the loop
		break
	# put back the cube in its initial state
	elif raw_in == 'z':
		cube = original_cube
		print("\033c")
		print(help)
		print_cube(cube)
	# execute the string of commands
	else:	
		cube = chain(raw_in, cube)
		print(help)
		print_cube(cube)
		print(fitness(cube))



