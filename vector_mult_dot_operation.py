myList = [1, 2, 3, 4]
print ('List = ', myList)

myCubes = []
for e in myList:
    myCubes.append(e**3)
print('Cubes = ', myCubes)

a_list = [1, 2]
b_list = [3, 4]

dot = 0
for (a, b) in zip (a_list, b_list):
    dot += (a * b)
print('Matrix dot i.e. sum of ({0} * {1}) = {2}'.format(a_list, b_list, dot))

print()
print('*** Following code needs NumPy library to be available ***')
print()

import numpy as np

# Easy to do Matrix operations in NumPy
np_array = np.array(myList)
print ('np list = ', np_array)

np_cubes = np_array ** 3
print('np cubes = ', np_cubes)

np_a = np.array(a_list)
np_b = np.array(b_list)

# dot operation #1
np_vector_mult_result = (np_a * np_b)
dot_1 = np_vector_mult_result.sum()     # Use the inbuild sum() for the Vector
print('dot 1 = ', dot_1)

# dot operation #2
dot_2 = np.sum(np_a * np_b)             # Use the mp.sum() method, passing the args
print('dot 2 = ', dot_2)

# dot operation #3
dot_3 = np.dot(np_a, np_b)              # Instead of #1 and #2, directly use np.dot() function
print('dot 3 = ', dot_3)
