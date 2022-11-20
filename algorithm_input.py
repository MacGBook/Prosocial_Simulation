
# READ ME:
# This algorithm determines how much to allocate to each of the four groups. 
# Paremeters section below explains what each parameter space means
# Algorithm returns two arrays:
    # First array is the available resources, i.e. the amount we allcate for each group
    # Second array is the threshold or minimum resources each group needs
# The index for each array is: [community 0, community 1, community 2, community 3]


# PARAMETERS:
# total_resources = the total amount of resources to allocate at a given stage
# nv_A = the niceness value assigned to community 0
# nv_B = the niceness value assigned to community 1
# nv_C = the niceness value assigned to community 2
# nv_D = the niceness value assigned to community 3
# aa = lower bound i.e. required resources of community 0
# bb = lower bound i.e. required resources of community 1
# cc = lower bound i.e. required resources of community 2
# dd = lower bound i.e. required resources of community 3

# REFERENCES: 
# https://realpython.com/linear-programming-python/

# NOTES TO MAC:
# Make sure output is in whole numbers (use round())

# IMPORTS
from scipy.optimize import linprog
from numpy import asarray

def algorithm_input(total_resources, nv_A, nv_B, nv_C, nv_D, aa, bb, cc, dd):
    
    denominator = nv_A + nv_B + nv_C + nv_D
    
    a_coe = nv_A
    b_coe = nv_B
    c_coe = nv_C
    d_coe = nv_D
    
    obj_a = nv_A // denominator # weight for group A
    obj_b = nv_B // denominator # weight for group B
    obj_c = nv_C // denominator # weight for group C
    obj_d = nv_D // denominator # weight for group D
    
    # OBJECTIVE FUNCTION
    # naturally maximization so we keep as is (not minimizing) 
    obj = [obj_a, obj_b, obj_c, obj_d]
    
    # CONSTRAINT
    
    lhs_eq = [[1, 1, 1, 1]] # [a, b, c, d]
    rhs_eq = [total_resources]
    
    bnd = [(aa, float("inf")), # bounds for group A
           (bb, float("inf")), # bounds for group B
           (cc, float("inf")), # bounds for group C
           (dd, float("inf"))] # bounds for group D
    
    opt = linprog(c=obj, A_ub=None, b_ub=None, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="revised simplex")
    
    available_resources = opt['x']
    
    for value in available_resources:
        round(value)
    
    required_resources = asarray(list([aa, bb, cc, dd]))
    
    # np array
    return available_resources, required_resources

# TEST EXAMPLE OF ALGORITHM

x = algorithm_input(500, 26, 35, 99, 240, 11, 5, 21, 11)
print(x)

# REMINDER: first array is available_resources, second array is required_resources!





