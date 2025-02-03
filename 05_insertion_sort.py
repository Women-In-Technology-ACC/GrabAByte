# Insertion Sort

# An insertion sort algorithm builds the final sorted array one
# element at a time by inserting each item into the correct position

#################################################################

# SET VARIABLES
# the array to be sorted
array = [12, 11, 13, 5, 6]

# THE LOOP
# insert each element into its correct position
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

# PRINT RESULTS
print("Sorted array is:", array)