# Bubble Sort

# Bubble Sort is a simple sorting algorithm that repeatedly steps
# through the list, compares adjacent items, and swaps them if they
# are in the wrong order.

#################################################################

# SET VARIABLES
# the array to be sorted
array = [64, 34, 25, 12, 22, 11, 90]

# THE LOOP
# repeatedly step through the array to sort it
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

# PRINT RESULTS
print("Sorted array is:", array)


#################################################################
# O NOTATION - Quadratic Time O(n^2)

# Quadratic time O notation represents an algorithm where every
# element interacts with every other element in a nested loop


# # UNCOMMENT HERE DOWN
# # Initialize the iterations sum variable
# iterations = 0

# # Get the length of the array
# # n = len(array)
# n = 1000

# # Loop through each element n times
# for i in range(n):
#     for j in range(n-i-1):
#         iterations += 1

# # PRINT RESULTS
# print("The total iterations are: ", iterations)