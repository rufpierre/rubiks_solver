from engine import *

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

# static mode
if (not cli):
	rand_inst = "flfTrtffllTLbDBllt"
	pons_asinorum = "F2 B2 R2 L2 U2 D2"
	cube_in_a_cube = "F L F U' R U F2 L2 U' L' B D' B' L2 U"
	cube = chain(cube_in_a_cube, cube)
	print_cube(cube)

# CLI mode
while cli:
	raw_in = raw_input()
	# quit
	if raw_in == 'q':
		# clena screen
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



