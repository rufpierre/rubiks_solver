import copy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKRREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BLUE = '\033[44m'
    GREEN = '\033[102m'
    WHITE = '\033[47m'
    RED = '\033[101m'
    BLUE = '\033[104m'
#    ORANGE = '\033[41m'
    ORANGE = '\033[43m'
    YELLOW = '\033[103m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

cube = bcolors.WARNING+"""
    UUU
    UUU
    UUU
LLL FFF RRR BBB
LLL FFF RRR BBB
LLL FFF RRR BBB
    DDD
    DDD
    DDD
""" + bcolors.ENDC

cube_string = """
    {U0}{U1}{U2}
    {U3}{U4}{U5}
    {U6}{U7}{U8}

{L0}{L1}{L2} {F0}{F1}{F2} {R0}{R1}{R2} {B0}{B1}{B2}
{L3}{L4}{L5} {F3}{F4}{F5} {R3}{R4}{R5} {B3}{B4}{B5}
{L6}{L7}{L8} {F6}{F7}{F8} {R6}{R7}{R8} {B6}{B7}{B8}

    {D0}{D1}{D2}
    {D3}{D4}{D5}
    {D6}{D7}{D8}
"""

W = 1
G = 2
R = 3
B = 4
O = 5
Y = 6

def col(color):
	return bcolors.WHITE

colors = {W:bcolors.WHITE, G:bcolors.GREEN, R:bcolors.RED, B:bcolors.BLUE, O:bcolors.ORANGE, Y:bcolors.YELLOW}

original_cube = [
[W,W,W,
W,W,W,
W,W,W],
[G,G,G,
G,G,G,
G,G,G],
[R,R,R,
R,R,R,
R,R,R],
[B,B,B,
B,B,B,
B,B,B],
[O,O,O,
O,O,O,
O,O,O],
[Y,Y,Y,
Y,Y,Y,
Y,Y,Y],
]

cube_ = [
[W,W,W,
W,W,W,
W,G,Y],
[G,G,R,
G,G,B,
G,G,O],
[R,B,G,
O,R,Y,
B,Y,R],
[B,B,B,
O,B,B,
R,B,B],
[O,O,O,
O,O,O,
O,O,O],
[Y,W,G,
Y,Y,Y,
Y,Y,Y],
]

cube = original_cube

def print_cube(cube):
	print(cube_string.format(
		U0=colors[cube[0][0]]+"U"+bcolors.ENDC,
		U1=colors[cube[0][1]]+"U"+bcolors.ENDC,
		U2=colors[cube[0][2]]+"U"+bcolors.ENDC,
		U3=colors[cube[0][3]]+"U"+bcolors.ENDC,
		U4=colors[cube[0][4]]+"U"+bcolors.ENDC,
		U5=colors[cube[0][5]]+"U"+bcolors.ENDC,
		U6=colors[cube[0][6]]+"U"+bcolors.ENDC,
		U7=colors[cube[0][7]]+"U"+bcolors.ENDC,
		U8=colors[cube[0][8]]+"U"+bcolors.ENDC,
		L0=colors[cube[1][0]]+"L"+bcolors.ENDC,
		L1=colors[cube[1][1]]+"L"+bcolors.ENDC,
		L2=colors[cube[1][2]]+"L"+bcolors.ENDC,
		L3=colors[cube[1][3]]+"L"+bcolors.ENDC,
		L4=colors[cube[1][4]]+"L"+bcolors.ENDC,
		L5=colors[cube[1][5]]+"L"+bcolors.ENDC,
		L6=colors[cube[1][6]]+"L"+bcolors.ENDC,
		L7=colors[cube[1][7]]+"L"+bcolors.ENDC,
		L8=colors[cube[1][8]]+"L"+bcolors.ENDC,
		F0=colors[cube[2][0]]+"F"+bcolors.ENDC,
		F1=colors[cube[2][1]]+"F"+bcolors.ENDC,
		F2=colors[cube[2][2]]+"F"+bcolors.ENDC,
		F3=colors[cube[2][3]]+"F"+bcolors.ENDC,
		F4=colors[cube[2][4]]+"F"+bcolors.ENDC,
		F5=colors[cube[2][5]]+"F"+bcolors.ENDC,
		F6=colors[cube[2][6]]+"F"+bcolors.ENDC,
		F7=colors[cube[2][7]]+"F"+bcolors.ENDC,
		F8=colors[cube[2][8]]+"F"+bcolors.ENDC,
		R0=colors[cube[3][0]]+"R"+bcolors.ENDC,
		R1=colors[cube[3][1]]+"R"+bcolors.ENDC,
		R2=colors[cube[3][2]]+"R"+bcolors.ENDC,
		R3=colors[cube[3][3]]+"R"+bcolors.ENDC,
		R4=colors[cube[3][4]]+"R"+bcolors.ENDC,
		R5=colors[cube[3][5]]+"R"+bcolors.ENDC,
		R6=colors[cube[3][6]]+"R"+bcolors.ENDC,
		R7=colors[cube[3][7]]+"R"+bcolors.ENDC,
		R8=colors[cube[3][8]]+"R"+bcolors.ENDC,
		B0=colors[cube[4][0]]+"B"+bcolors.ENDC,
		B1=colors[cube[4][1]]+"B"+bcolors.ENDC,
		B2=colors[cube[4][2]]+"B"+bcolors.ENDC,
		B3=colors[cube[4][3]]+"B"+bcolors.ENDC,
		B4=colors[cube[4][4]]+"B"+bcolors.ENDC,
		B5=colors[cube[4][5]]+"B"+bcolors.ENDC,
		B6=colors[cube[4][6]]+"B"+bcolors.ENDC,
		B7=colors[cube[4][7]]+"B"+bcolors.ENDC,
		B8=colors[cube[4][8]]+"B"+bcolors.ENDC,
		D0=colors[cube[5][0]]+"D"+bcolors.ENDC,
		D1=colors[cube[5][1]]+"D"+bcolors.ENDC,
		D2=colors[cube[5][2]]+"D"+bcolors.ENDC,
		D3=colors[cube[5][3]]+"D"+bcolors.ENDC,
		D4=colors[cube[5][4]]+"D"+bcolors.ENDC,
		D5=colors[cube[5][5]]+"D"+bcolors.ENDC,
		D6=colors[cube[5][6]]+"D"+bcolors.ENDC,
		D7=colors[cube[5][7]]+"D"+bcolors.ENDC,
		D8=colors[cube[5][8]]+"D"+bcolors.ENDC,
		))


def self_clockwise(facet, cube, new_cube):
	new_cube[facet][2] = cube[facet][0]
	new_cube[facet][5] = cube[facet][1]
	new_cube[facet][8] = cube[facet][2]
	new_cube[facet][1] = cube[facet][3]
	new_cube[facet][7] = cube[facet][5]
	new_cube[facet][0] = cube[facet][6]
	new_cube[facet][3] = cube[facet][7]
	new_cube[facet][6] = cube[facet][8]

def self_counter_clockwise(facet, cube, new_cube):
	new_cube[facet][0] = cube[facet][2]
	new_cube[facet][1] = cube[facet][5]
	new_cube[facet][2] = cube[facet][8]
	new_cube[facet][3] = cube[facet][1]
	new_cube[facet][5] = cube[facet][7]
	new_cube[facet][6] = cube[facet][0]
	new_cube[facet][7] = cube[facet][3]
	new_cube[facet][8] = cube[facet][6]


def F(cube):
	new_cube = copy.deepcopy(cube)

	new_cube[3][0] = cube[0][6]
	new_cube[3][3] = cube[0][7]
	new_cube[3][6] = cube[0][8]
	new_cube[0][8] = cube[1][2]
	new_cube[0][7] = cube[1][5]
	new_cube[0][6] = cube[1][8]
	new_cube[1][2] = cube[5][0]
	new_cube[1][5] = cube[5][1]
	new_cube[1][8] = cube[5][2]
	new_cube[5][0] = cube[3][6]
	new_cube[5][1] = cube[3][3]
	new_cube[5][2] = cube[3][0]
	self_clockwise(2, cube, new_cube)	

	return copy.deepcopy(new_cube)

def rot_T(cube):
	new_cube = copy.deepcopy(cube)

	for i in range(9):
		new_cube[2][i] = cube[3][i]
		new_cube[3][i] = cube[4][i]
		new_cube[1][i] = cube[2][i]
		new_cube[4][i] = cube[1][i]
	self_clockwise(0, cube, new_cube)
	self_counter_clockwise(5, cube, new_cube)

	return copy.deepcopy(new_cube)

def rot_R(cube):
	new_cube = copy.deepcopy(cube)

	for i in range(9):
		# top takes front
		new_cube[0][i] = cube[2][i]
		# front takes down
	 	new_cube[2][i] = cube[5][i]

	# down takes back
	new_cube[5][8] = cube[4][0]
	new_cube[5][7] = cube[4][1]
	new_cube[5][6] = cube[4][2]
	new_cube[5][5] = cube[4][3]
	new_cube[5][4] = cube[4][4]
	new_cube[5][3] = cube[4][5]
	new_cube[5][2] = cube[4][6]
	new_cube[5][1] = cube[4][7]
	new_cube[5][0] = cube[4][8]

	# back takes top
	new_cube[4][8] = cube[0][0]
	new_cube[4][7] = cube[0][1]
	new_cube[4][6] = cube[0][2]
	new_cube[4][5] = cube[0][3]
	new_cube[4][4] = cube[0][4]
	new_cube[4][3] = cube[0][5]
	new_cube[4][2] = cube[0][6]
	new_cube[4][1] = cube[0][7]
	new_cube[4][0] = cube[0][8]

	self_clockwise(3, cube, new_cube)
	self_counter_clockwise(1, cube, new_cube)

	return copy.deepcopy(new_cube)



def R(cube):
	cube = rot_T(cube)
	cube = F(cube)
	cube = rot_T(cube)
	cube = rot_T(cube)
	cube = rot_T(cube)
	return cube

def B(cube):
	cube = rot_T(cube)
	cube = rot_T(cube)
	cube = F(cube)
	cube = rot_T(cube)
	cube = rot_T(cube)
	return cube

def L(cube):
	cube = rot_T(cube)
	cube = rot_T(cube)
	cube = rot_T(cube)
	cube = F(cube)
	cube = rot_T(cube)
	return cube

def D(cube):
	cube = rot_R(cube)
	cube = F(cube)
	cube = rot_R(cube)
	cube = rot_R(cube)
	cube = rot_R(cube)
	return cube

def U(cube):
	cube = rot_R(cube)
	cube = rot_R(cube)
	cube = rot_R(cube)
	cube = F(cube)
	cube = rot_R(cube)
	return cube

def split_instruction(instruction):
	"""split an instruction of form: "f'" into the tupple ("F",3), or "L2" into ('L', 2)"""
	if(len(instruction)==1):
		return instruction.upper(), 1
	else:
		instruction = instruction.replace("'","3")
		return instruction[0].upper(), int(instruction[1])

def transform(instruction, cube):
	"""apply an instruction of form f' (or l2, or R2) to a cube"""
	transformation, times = split_instruction(instruction)
	for i in range(times):
		cube = eval(transformation+"(cube)")
	return cube



def chain(instructions, cube):
	"""execute a chain of instructions in hte form of : 'F2 B2 R2 L2 U2 D2'"""
	print (instructions)
	for instruction in instructions.split():
		cube = transform(instruction,cube)
	return cube
