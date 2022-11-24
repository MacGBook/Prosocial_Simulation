
# GREEDY ALGORITHM 

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

from numpy import asarray

def greedy_algorithm(total_resources, nv_A, nv_B, nv_C, nv_D, aa, bb, cc, dd):
    
    denominator = nv_A + nv_B + nv_C + nv_D
    
    a_ratio = nv_A / denominator
    b_ratio = nv_B / denominator
    c_ratio = nv_C / denominator
    d_ratio = nv_D / denominator
    
    a_allocation = a_ratio * total_resources
    b_allocation = b_ratio * total_resources
    c_allocation = c_ratio * total_resources
    d_allocation = d_ratio * total_resources
    
    pre_list = list([a_allocation, b_allocation, c_allocation, d_allocation])
    post_list = []
    
    for value in pre_list:
        new = round(value)
        post_list.append(new)
    
    
    available_resources = asarray(post_list)

    required_resources = asarray(list([aa, bb, cc, dd]))
    
    return available_resources, required_resources

# TEST EXAMPLE OF ALGORITHM

x = greedy_algorithm(44, 26, 35, 99, 240, 11, 5, 21, 11)
print(x)

# REMINDER: first array is available_resources, second array is required_resources!

