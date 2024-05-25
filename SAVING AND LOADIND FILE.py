import numpy as np

# SAVING ANG WRITING FILE USING NUMPY

# 1 - Saving the array to a CSV File
my_array = np.array([[1, 18, 5], [8, 17, 5], [8, 29, 5]])
np.save('array.csv', my_array)

print()

# 2 - Saving the array to a Binary File
my_array = np.array([["karl"], ["steve"], ["bulosan"]])
np.save('array.npy', my_array)

print()

# 3 -  Saving the arrays to a Compressed File
my_array1 = np.array([[6, 3, 9], [0, 7, 1]])
my_array2 = np.array([[9, 6, 6], [0, 9, 8]])
np.savez_compressed('arrays.npz', array1=my_array1, array2=my_array2)

print()

# LOADING DATA FROM FILES USING NUMPY

# 1 - Loading the array from a CSV File
my_array = np.loadtxt('array.csv')
print("Here it is:", my_array)

print()

# 2 - Loading the array from a Binary File
my_array = np.load('array.npy')
print("Here it is:", my_array)

print()

# 3 - Loading the arrays from a compressed file
my_array = np.load('arrays.npz')
my_array1 = my_array['array1']
my_array2 = my_array['array2']
print("Here it is:", my_array1, my_array2)
