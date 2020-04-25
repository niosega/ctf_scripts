from z3 import *

# Init the solver.
s = Solver()
INPUT_LEN=3

######## SPECIFIC CONSTRAINT ########
def add_constraint(X, s):
    """ Define here your constraint."""
    pass
#####################################

######## GENERIC CONSTRAINT #########
def range_constraint(s, a, b):
    for i in range(INPUT_LEN):
        s.add(X[i] >= a)
        s.add(X[i] <= b)

def upper_case(s):
    range_constraint(s, 0x41, 0x5A)

def lower_case(s):
    range_constraint(s, 0x61, 0x7A)

def printable(s):
    range_constraint(s, 0x21, 0x7E)

def number(s):
    range_constraint(s, 0x30, 0x39)
#####################################


# Init the input vector.
X = []
n = 8
for i in range(INPUT_LEN):
	X.append(BitVec('X_%d'%(i), n))

# Add specific constraint.
add_constraint(X, s)

# Generate solutions.
nb_sol = 0
while s.check() == sat:
    # Convert the model to string.
    flag =''
    for i in range(INPUT_LEN):
        x = chr(int(str(s.model()[X[i]])))
        flag += x

    # Print the solution and increment the nb_sol counter.
    print(flag)
    nb_sol += 1

    # Avoid finding the same solution.
    a = []
    for i in range(len(flag)):
        a.append(X[i] != ord(flag[i]))
    s.add(Or(a))

print("Number of solutions: ", nb_sol)